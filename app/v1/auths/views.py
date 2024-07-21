from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.jwt_builder import JwtBuilder
from app.models import Employee,Customer,Organization,Role
from app.serializers.employee import EmployeeInSerializer,EmployeeOutSerializer
from app.serializers.customer import CustomerInSerializer,CustomerOutSerializer
from utils.id_generator import generate_unique_id
from utils import exceptions
from utils.decorators.authorize import is_authorize
from django.contrib.auth.hashers import make_password
from utils.decorators.authorize import is_authorize

class RegisterView(APIView):

    @is_authorize(role=['ADMIN','MANAGER'])
    def post(self,request):
        token_data=request.token_data
        data=request.data
        user_type=data.get("user_type").lower()

        user_id=generate_unique_id()
        tokens={}

        if user_type=="employee":
            serializer=EmployeeInSerializer(data=data)
            if serializer.is_valid():
                data=serializer.validated_data
            else:
                return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            try:
                role=Role.objects.get(role_id=data.get('role_id'))
            except Role.DoesNotExist:
                raise exceptions.NotExists(detail="Role doesn't exists!")
            
            try:
                organization=Organization.objects.get(org_id=token_data.get('org_id'))
            except Organization.DoesNotExist:
                raise exceptions.NotExists(detail="organization doesn't exists!")
            
            employee=Employee(
                emp_id=user_id,
                name=data.get('name'),
                organization=organization,
                role=role,
                mobile=data.get('mobile'),
                email=data.get('email'),
                password=data.get('password')
            )

            employee.save()
            user=EmployeeOutSerializer(instance=employee).data

            jwt_payload={
                "user_id":user_id,
                "role":role.name,
                "user_type":"employee",
                "org_id":employee.organization.org_id,
                "is_verified":False
            }

            tokens=JwtBuilder(payload=jwt_payload).get_token()
        
        elif user_type=="customer":
            serializer=CustomerInSerializer(data=data)
            if serializer.is_valid():
                data=serializer.validated_data
            else:
                return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            if Customer.objects.filter(organization__org_id=token_data.get('org_id'),mobile=data.get('mobile')).exists() or (data.get('email') and Customer.objects.filter(organization__org_id=token_data.get('org_id'),email=data.get('email')).exists()):
                raise exceptions.GenericException(detail="customer already exists!",code=400)

            customer=Customer(
                cust_id=user_id,
                organization=Organization.objects.get(org_id=token_data.get('org_id')),
                name=data.get('name'),
                mobile=data.get('mobile'),
                email=data.get('email'),
                address=data.get('address')
            )

            customer.save()
            user=CustomerOutSerializer(instance=customer).data

        return Response({"message":"registered!","token":tokens if tokens else {},"user":user},status=status.HTTP_201_CREATED)

class LoginView(APIView):

    def post(self,request):
        data=request.data
        user_type=data.get("user_type").lower()
        username=data.get('username') # might be email or mobile
        password=data.get('password')

        if user_type=="employee":

            if Employee.objects.filter(email=username).exists():
                employee=Employee.objects.get(email=username)
            
            elif Employee.objects.filter(mobile=username).exists():
                employee=Employee.objects.get(mobile=username)
            
            else:
                raise exceptions.NotExists(detail="email or mobile not exists!")
            
            
            if not employee.is_correct_password(password):
                raise exceptions.GenericException(
                    detail="Wrong password!",
                    code=400
                )

            jwt_payload={
                "user_id":employee.emp_id,
                "role":employee.role.name,
                "user_type":"employee",
                "org_id":employee.organization.org_id,
                "is_verified":True if employee.verified_at else False
            }

            tokens=JwtBuilder(payload=jwt_payload).get_token()
        
        return Response({"message":"login!","token":tokens if tokens else {}},status=status.HTTP_200_OK)


class RefreshTokenView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        user_id=token_data.get('user_id')
        user_type=token_data.get('user_type').lower()

        if user_type=="employee":

            try:
                employee=Employee.objects.get(emp_id=user_id)
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="user doesn't exists!")
            
            jwt_payload={
                "user_id":employee.emp_id,
                "role":employee.role.name,
                "user_type":"employee",
                "org_id":employee.organization.org_id,
                "is_verified":True if employee.verified_at else False
            }

            tokens=JwtBuilder(payload=jwt_payload).get_token()
        
        return Response({"message":"new tokens!","token":tokens},status=status.HTTP_201_CREATED)


class ForgetPasswordView(APIView):

    def post(self,request):
        data=request.data
        user_type=data.get("user_type").lower()
        username=data.get('username') # might be email or mobile
        new_password=data.get('new_password')

        if user_type=="employee":

            if Employee.objects.filter(email=username).exists():
                employee=Employee.objects.get(email=username)
            
            elif Employee.objects.filter(mobile=username).exists():
                employee=Employee.objects.get(mobile=username)
            
            else:
                raise exceptions.NotExists(detail="email or mobile not exists!")
            
            employee.password=make_password(new_password)
            employee.save()
        
        return Response({"message":"password is updated!"},status=status.HTTP_200_OK)