from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Order,PaymentMode,Customer,Organization,Billing,OrderMapToBilling,Employee,GSTRates
from utils.id_generator import generate_unique_id
from utils import exceptions
from django.db import transaction
from .invoice_generate import Invoice
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from app.serializers.billing import BillingInSerializer,BillingOutWithCustSerializer,BillingUpdateSerializer,BillingDeleteSerializer

class BillingView(APIView):

    @is_authorize(role=['ADMIN','MANAGER'])
    def get(self,request):
        token_data=request.token_data
        query_params=request.query_params

        if 'bill-id' in query_params:
            try:
                bill=Billing.objects.get(bill_id=query_params['bill-id'])
            except Billing.DoesNotExist:
                raise exceptions.NotExists(detail="bill doesn't exists!")
            
            data=BillingOutWithCustSerializer(instance=bill).data

            return Response({"billing":data},status=status.HTTP_200_OK)
            

        if not ('page-size' in query_params and 'page' in query_params):
            raise exceptions.GenericException(
                detail="pass page and page-size in query params!",
                code=400
            )
        if 'customer-id' in query_params:
            customer_id=query_params['customer-id']
            billings=Billing.objects.filter(organization__org_id=token_data.get('org_id'),customer__cust_id=customer_id).order_by('-billing_date')
        else:
            billings=Billing.objects.filter(organization__org_id=token_data.get('org_id')).order_by('-billing_date')

        paginator=Paginator(billings,int(query_params['page-size']))

        try:
            billing=paginator.page(int(query_params['page']))
        except PageNotAnInteger:
            billing=paginator.page(1)
        except EmptyPage:
            billing=[]
        
        data=BillingOutWithCustSerializer(instance=billing,many=True).data

        return Response({"billings":data},status=status.HTTP_200_OK)
    
    @is_authorize(role=['ADMIN','MANAGER'])
    def post(self,request):
        token_data=request.token_data
        serializer=BillingInSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data
            with transaction.atomic():
                billing_price=0
                discount=0
                orders=[]

                try:
                    customer=Customer.objects.get(cust_id=data.get('customer_id'))
                except Customer.DoesNotExist:
                    raise exceptions.NotExists(detail="customer doesn't exists!")
                
                try:
                    payment_mode=PaymentMode.objects.get(mode_id=data.get('payment_mode'))
                except PaymentMode.DoesNotExist:
                    raise exceptions.NotExists(detail="payment mode doesn't exists!")
                
                try:
                    billed_by=Employee.objects.get(emp_id=token_data.get('user_id'))
                except PaymentMode.DoesNotExist:
                    raise exceptions.NotExists(detail="employee doesn't exists!")
                
                try:
                    organization=Organization.objects.get(org_id=token_data.get('org_id'))
                except Organization.DoesNotExist:
                    raise exceptions.NotExists(detail="organization doesn't exists!")
                
                for _data in data.get('orders'):

                    try:
                        order=Order.objects.get(order_id=_data.get('order_id'))
                        orders.append(order)
                    except Order.DoesNotExist:
                        raise exceptions.NotExists(detail="order doesn't exists!")
                    
                    product=order.product

                    billing_price+=order.quantity*product.price
                
                    discount+=order.quantity*product.discount if product.discount else 0

                discounted_price=(billing_price-((billing_price*discount)/100)) if discount else billing_price
                
                try:
                    gst_rates=GSTRates.objects.get(pk=1)
                except GSTRates.DoesNotExist:
                    raise exceptions.NotExists(detail="gst rates doesn't exists!")
                
                if data.get('is_inter_state'):
                    # Calculate IGST amount
                    igst_amount = discounted_price * (gst_rates.igst / 100)
                    cgst_amount = 0
                    sgst_amount = 0
                    cgst_rates = 0
                    sgst_rates = 0
                    igst_rates=gst_rates.igst
                    total_amount_incl_gst = discounted_price + igst_amount
                else:
                    # Calculate CGST and SGST amounts
                    cgst_amount = discounted_price * (gst_rates.cgst / 100)
                    sgst_amount = discounted_price * (gst_rates.sgst / 100)
                    igst_amount = 0
                    cgst_rates = gst_rates.cgst
                    sgst_rates = gst_rates.sgst
                    igst_rates=0
                    # Calculate total amount including CGST and SGST
                    total_amount_incl_gst = discounted_price + cgst_amount + sgst_amount

                bill_id=generate_unique_id()

                bill=Billing(
                    bill_id=bill_id,
                    organization=organization,
                    billed_by=billed_by,
                    customer=customer,
                    payment_mode=payment_mode,
                    discount=discount,
                    total_amount=billing_price,
                    discounted_price=discounted_price,
                    cgst_amount=cgst_amount,
                    sgst_amount=sgst_amount,
                    igst_amount=igst_amount,
                    cgst_rates=cgst_rates,
                    sgst_rates=sgst_rates,
                    igst_rates=igst_rates,
                    is_inter_state=data.get('is_inter_state'),
                    taxable_amount=total_amount_incl_gst
                )
                invoice=Invoice(
                    template_name='invoice.html',
                    to=customer.email,
                    name=customer.name
                )
                invoice_path,invoice_id=invoice.generate(bill=bill,orders=orders)
                bill.invoice=invoice_id
                bill.invoice_path=invoice_path
                bill.save()

                for order in orders:
                    OrderMapToBilling.objects.create(
                        order=order,
                        billing=bill
                    )
                
            data=BillingOutWithCustSerializer(instance=bill,many=False).data
            return Response({"billing":data},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    @is_authorize(role=['ADMIN','MANAGER'])
    def delete(self,request):
        token_data=request.token_data
        serializer=BillingDeleteSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.validated_data
            try:
                bill=Billing.objects.get(bill_id=data.get('bill_id'))
            except Billing.DoesNotExist:
                raise exceptions.NotExists(detail="bill doesn't exists!")
            bill.delete()
            return Response({"message":"bill is deleted!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
