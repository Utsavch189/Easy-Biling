from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Employee,Organization,Role
from app.serializers.employee import EmployeeOutSerializer,EmployeeUpdateSerializer,EmployeeDeleteSerializer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from utils import exceptions
from datetime import datetime

class EmployeeView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if 'employee-id' in query_params:
            try:
                employee=Employee.objects.get(emp_id=token_data.get('user_id'))
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="employee doesn't exists!")
            
            data=EmployeeOutSerializer(instance=employee,many=False).data
            return Response({"employee":data},status=status.HTTP_200_OK)

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        employees=Employee.objects.filter(organization__org_id=token_data.get('org_id'))
        paginator=Paginator(employees,int(query_params['page-size']))

        try:
            employee=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            employee=paginator.page(1)
        except EmptyPage:
            employee=[]
        
        data=EmployeeOutSerializer(instance=employee,many=True).data
        return Response({"employees":data},status=status.HTTP_200_OK)

        
        
    @is_authorize()
    def put(self,request):
        token_data=request.token_data
        serializer=EmployeeUpdateSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data

            try:
                role=Role.objects.get(role_id=data.get('role_id'))
            except Role.DoesNotExist:
                raise exceptions.NotExists(detail="Role doesn't exists!")
            
            try:
                organization=Organization.objects.get(org_id=token_data.get('org_id'))
            except Organization.DoesNotExist:
                raise exceptions.NotExists(detail="organization doesn't exists!")
            
            try:
                employee=Employee.objects.get(emp_id=data.get('emp_id'))
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="user doesn't exists!")
            
            employee.organization=organization
            employee.role=role
            employee.name=data.get('name')
            employee.mobile=data.get('mobile')
            employee.email=data.get('email')
            employee.updated_at=datetime.now()
            employee.save()

            data=EmployeeOutSerializer(instance=employee,many=False).data
            return Response({"employee":data},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        serializer=EmployeeDeleteSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data
            try:
                employee=Employee.objects.get(emp_id=data.get('emp_id'))
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="user doesn't exists!")
            name=employee.name
            employee.delete()
            return Response({"message":f"Employee {name} is deleted!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
