from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Product,Organization,ProductType
from app.serializers.product import ProductInSerializer,ProductOutSerializer,ProductUpdateSerializer,ProductDeleteSerializer
from app.serializers.product_type import ProductTypeDeleteSerializer,ProductTypeInSerializer,ProductTypeOutSerializer,ProductTypeUpdateSerializer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from utils import exceptions
from datetime import datetime
from utils.id_generator import generate_unique_id

class ProductView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        
        if not Organization.objects.filter(org_id=token_data.get('org_id')).exists():
            raise exceptions.NotExists(detail="Organization doesn't exists!")
        
        if 'product-type' in query_params:
            product_type=query_params['product-type']
            products=Product.objects.filter(organization__org_id=token_data.get('org_id'),types__p_type_id=product_type)
        else:
            products=Product.objects.filter(organization__org_id=token_data.get('org_id'))
        
        paginator=Paginator(products,int(query_params['page-size']))

        try:
            product=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            product=paginator.page(1)
        except EmptyPage:
            product=[]
        
        data=ProductOutSerializer(instance=product,many=True).data

        return Response({"products":data},status=status.HTTP_200_OK)

    @is_authorize(role=['ADMIN','MANAGER'])
    def post(self,request):
        serializer=ProductInSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data

            if not Organization.objects.filter(org_id=data.get('org_id')).exists():
                raise exceptions.NotExists(detail="Organization doesn't exists!")
            
            product=Product(
                p_id=generate_unique_id(),
                organization=Organization.objects.get(org_id=data.get('org_id')),
                name=data.get('name'),
                types=ProductType.objects.get(p_type_id=data.get('types')) if data.get('types') else None,
                desc=data.get('desc'),
                price=data.get('price'),
                discount=data.get('discount')
            )
            product.save()

            data=ProductOutSerializer(instance=product,many=False).data
            return Response({"product":data},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        
    @is_authorize(role=['ADMIN','MANAGER'])
    def put(self,request):
        serializer=ProductUpdateSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data

            if not Organization.objects.filter(org_id=data.get('org_id')).exists():
                raise exceptions.NotExists(detail="Organization doesn't exists!")
            
            if not Product.objects.filter(p_id=data.get('p_id')).exists():
                raise exceptions.NotExists(detail="Product doesn't exists!")

            product=Product.objects.get(p_id=data.get('p_id'))
            product.organization=Organization.objects.get(org_id=data.get('org_id'))
            product.name=data.get('name')
            if data.get('types'):
                if not ProductType.objects.filter(p_type_id=data.get('types')).exists():
                    raise exceptions.NotExists(detail="Product Type doesn't exists!")
                product.types=ProductType.objects.get(p_type_id=data.get('types'))
            product.desc=data.get('desc')
            product.price=data.get('price')
            product.discount=data.get('discount')
            product.is_active=data.get('is_active')
            product.is_available=data.get('is_available')
            product.updated_at=datetime.now()
            product.save()

            data=ProductOutSerializer(instance=product,many=False).data
            return Response({"product":data},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        serializer=ProductDeleteSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data

            if not Product.objects.filter(p_id=data.get('p_id')).exists():
                raise exceptions.NotExists(detail="Product doesn't exists!")
            
            product=Product.objects.get(p_id=data.get('p_id'))
            name=product.name
            product.delete()
            return Response({"message":f"Product {name} is deleted!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ProductTypeView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        
        if not Organization.objects.filter(org_id=token_data.get('org_id')).exists():
                raise exceptions.NotExists(detail="Organization doesn't exists!")
        
        product_types=ProductType.objects.filter(organization__org_id=token_data.get('org_id'))
        paginator=Paginator(product_types,int(query_params['page-size']))

        try:
            product_type=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            product_type=paginator.page(1)
        except EmptyPage:
            product_type=[]
        
        data=ProductTypeOutSerializer(instance=product_type,many=True).data

        return Response({"product_types":data},status=status.HTTP_200_OK)

    @is_authorize(role=['ADMIN','MANAGER'])
    def post(self,request):
        serializer=ProductTypeInSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data

            if not Organization.objects.filter(org_id=data.get('org_id')).exists():
                raise exceptions.NotExists(detail="Organization doesn't exists!")
            
            product_type=ProductType(
                p_type_id=generate_unique_id(),
                name=data.get('name'),
                organization=Organization.objects.get(org_id=data.get('org_id')),
                desc=data.get('desc')
            )
            product_type.save()
            data=ProductTypeOutSerializer(instance=product_type,many=False).data
            return Response({"product_type":data},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        
    @is_authorize(role=['ADMIN','MANAGER'])
    def put(self,request):
        serializer=ProductTypeUpdateSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data

            if not Organization.objects.filter(org_id=data.get('org_id')).exists():
                raise exceptions.NotExists(detail="Organization doesn't exists!")
            
            if not ProductType.objects.filter(p_type_id=data.get('p_type_id')).exists():
                raise exceptions.NotExists(detail="Product Type doesn't exists!")

            product_type=ProductType.objects.get(p_type_id=data.get('p_type_id'))
            product_type.organization=Organization.objects.get(org_id=data.get('org_id'))
            product_type.name=data.get('name')
            product_type.desc=data.get('desc')
            product_type.is_active=data.get('is_active')
            product_type.updated_at=datetime.now()
            product_type.save()

            data=ProductTypeOutSerializer(instance=product_type,many=False).data
            return Response({"product_type":data},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        serializer=ProductTypeDeleteSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data

            if not ProductType.objects.filter(p_type_id=data.get('p_type_id')).exists():
                raise exceptions.NotExists(detail="Product Type doesn't exists!")
            
            product_type=ProductType.objects.get(p_type_id=data.get('p_type_id'))
            name=product_type.name
            product_type.delete()
            return Response({"message":f"Product Type {name} is deleted!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)