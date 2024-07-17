from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Order,Product,Customer,Organization
from app.serializers.order import OrderInSerializer,OrderOutSerializer,OrderUpdateSerializer,OrderDeleteSerializer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from utils import exceptions
from datetime import datetime
from utils.id_generator import generate_unique_id
from django.db import transaction

class OrderView(APIView):

    @is_authorize(role=['ADMIN','MANAGER'])
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        if 'customer-id' in query_params:
            customer_id=query_params['customer-id']
            orders=Order.objects.filter(organization__org_id=token_data.get('org_id'),customer__cust_id=customer_id).order_by('-order_date')
        else:
            orders=Order.objects.filter(organization__org_id=token_data.get('org_id')).order_by('-order_date')

        paginator=Paginator(orders,int(query_params['page-size']))

        try:
            order=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            order=paginator.page(1)
        except EmptyPage:
            order=[]
        
        data=OrderOutSerializer(instance=order,many=True).data

        return Response({"orders":data},status=status.HTTP_200_OK)
    
    @is_authorize(role=['ADMIN','MANAGER'])
    def post(self,request):
        token_data=request.token_data
        serializer=OrderOutSerializer(data=request.data,many=True)

        if serializer.is_valid():
            data=serializer.validated_data
            orders=[]
            with transaction.atomic():
                for _order in data:

                    if not Customer.objects.filter(organization__org_id=token_data.get('org_id'),mobile=_order.get('customer_phone')).exists():
                        raise exceptions.NotExists(detail="customer doesn't exists!")

                    if not Product.objects.filter(p_id=data.get('product_id')).exists():
                        raise exceptions.NotExists(detail="product doesn't exists!")

                    if _order.get('customer_phone'):
                        customer=Customer.objects.filter(organization__org_id=token_data.get('org_id'),mobile=_order.get('customer_phone'))[0]
                    elif _order.get('customer_id'):
                        customer=Customer.objects.get(cust_id=_order.get('customer_id'))
                    else:
                        raise exceptions.Unprocessable(detail="customer phone no or id must be provided!")

                    order=Order(
                        order_id=generate_unique_id(),
                        organization=Organization.objects.get(org_id=token_data.get('org_id')),
                        customer=customer,
                        product=Product.objects.get(p_id=_order.get('product_id')),
                        quantity=_order.get('quantity')
                    )
                    order.save()
                    orders.append(order)

            data=OrderOutSerializer(instance=orders,many=True).data
            return Response({"orders":data},status=status.HTTP_201_CREATED)

        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @is_authorize(role=['ADMIN','MANAGER'])
    def put(self,request):
        token_data=request.token_data
        serializer=OrderUpdateSerializer(data=request.data,many=True)
        if serializer.is_valid():
            data=serializer.validated_data

            if not Order.objects.filter(order_id=data.get('order_id')).exists():
                raise exceptions.NotExists(detail="Order doesn't exists!")

            order=Order.objects.get(order_id=data.get('order_id'))
            
            if not Customer.objects.filter(organization__org_id=token_data.get('org_id'),mobile=data.get('customer_phone')).exists():
                raise exceptions.NotExists(detail="customer doesn't exists!")
            
            if not Product.objects.filter(p_id=data.get('product_id')).exists():
                raise exceptions.NotExists(detail="product doesn't exists!")

            if data.get('customer_phone'):
                customer=Customer.objects.filter(organization__org_id=token_data.get('org_id'),mobile=data.get('customer_phone'))[0]
            elif data.get('customer_id'):
                customer=Customer.objects.get(cust_id=data.get('customer_id'))
            else:
                raise exceptions.Unprocessable(detail="customer phone no or id must be provided!")
            
            product=Product.objects.get(p_id=data.get('product_id'))

            order.customer=customer
            order.product=product
            order.quantity=data.get('quantity')
            order.is_active=data.get('is_active')
            order.updated_at=datetime.now()
            order.save()

            data=OrderOutSerializer(instance=order,many=False).data
            return Response({"order":data},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        token_data=request.token_data
        serializer=OrderDeleteSerializer(data=request.data,many=True)
        if serializer.is_valid():
            data=serializer.validated_data

            if not Order.objects.filter(order_id=data.get('order_id')).exists():
                raise exceptions.NotExists(detail="Order doesn't exists!")
            
            order=Order.objects.get(order_id=data.get('order_id'))
            order.delete()
            return Response({"message":"order is deleted!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)