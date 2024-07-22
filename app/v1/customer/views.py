from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Customer,Organization
from app.serializers.customer import CustomerOutSerializer,CustomerUpdateSerializer,CustomerDeleteSerializer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from utils import exceptions
from datetime import datetime

class CustomerView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if 'customer-id' in query_params:
            try:
                customer=Customer.objects.get(cust_id=query_params['customer-id'])
            except Customer.DoesNotExist:
                raise exceptions.NotExists(detail="customer doesn't exists!")
            
            data=CustomerOutSerializer(instance=customer,many=False).data
            return Response({"customer":data},status=status.HTTP_200_OK)

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        customers=Customer.objects.filter(organization__org_id=token_data.get('org_id'))
        paginator=Paginator(customers,int(query_params['page-size']))

        try:
            _customer=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            _customer=paginator.page(1)
        except EmptyPage:
            _customer=[]
        
        data=CustomerOutSerializer(instance=_customer,many=True).data
        return Response({"customers":data},status=status.HTTP_200_OK)

        
        
    @is_authorize()
    def put(self,request):
        token_data=request.token_data
        serializer=CustomerUpdateSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data
            
            try:
                organization=Organization.objects.get(org_id=token_data.get('org_id'))
            except Organization.DoesNotExist:
                raise exceptions.NotExists(detail="organization doesn't exists!")
            
            try:
                customer=Customer.objects.get(cust_id=data.get('cust_id'))
            except Customer.DoesNotExist:
                raise exceptions.NotExists(detail="customer doesn't exists!")
            
            customer.organization=organization
            customer.name=data.get('name')
            customer.mobile=data.get('mobile')
            customer.email=data.get('email')
            customer.updated_at=datetime.now()
            customer.save()

            data=CustomerOutSerializer(instance=customer,many=False).data
            return Response({"employee":data},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        serializer=CustomerDeleteSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data

            try:
                customer=Customer.objects.get(cust_id=data.get('cust_id'))
            except Customer.DoesNotExist:
                raise exceptions.NotExists(detail="customer doesn't exists!")

            customer.is_active=True
            customer.save()

            return Response({"message":f"Customer {customer.name} is deleted!","id":customer.cust_id},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
