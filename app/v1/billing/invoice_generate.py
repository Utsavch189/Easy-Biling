from django.template.loader import render_to_string
from utils.emails import SendMail
from multiprocessing import Process
from app.models import Billing,Order
import time
import datetime
from typing import List

class Invoice:

    def __init__(self,template_name:str,to:str,name:str) -> None:
        self.template_name=template_name
        self.to=to
        self.name=name
    
    def generate(self,bill:Billing,orders:List[Order]):
        try:
            invoice='INV'+str(int(time.time() * 1000))

            if Billing.objects.filter(invoice=invoice).exists():
                raise Exception("non unique billing invoice id")
            
            context={
                "invoice":invoice,
                "invoice_date": datetime.datetime.now().strftime('%d-%m-%Y'),
                "org_name":bill.organization.name,
                "org_address":bill.organization.address,
                "cust_name":bill.customer.name,
                "cust_address":bill.customer.address,
                "payment_mode":bill.payment_mode.name,
                "total_amount":round(bill.total_amount,2),
                "discount_percentage":round(bill.discount,2),
                "discount_amount":round(bill.discounted_price,2),
                "is_inter_state":bill.is_inter_state,
                "igst_rate":round(bill.igst_rates,2),
                "igst_amount":round(bill.igst_amount,2),
                "cgst_rate":round(bill.cgst_rates,2),
                "cgst_amount":round(bill.cgst_amount,2),
                "sgst_rate":round(bill.sgst_rates,2),
                "sgst_amount":round(bill.sgst_amount,2),
                "total_incl_tax":round(bill.taxable_amount,2),
                "associate_orders":[
                    {"product_name":order.product.name,"quantity":order.quantity,
                     "product_per_price":round(order.product.price,2),"product_per_discount":round(order.product.discount,2),
                     "total_price":round(order.quantity*((order.product.price-((order.product.price*order.product.discount)/100)) if order.product.discount else order.product.price),2)
                    } for order in orders
                ]
            }
            rendered_template=render_to_string(self.template_name,context)
            invoice_path=f"media/invoices/{invoice}.html"

            with open(invoice_path,'w') as inv:
                inv.write(rendered_template)

            subject=f"Hello {self.name}, please check your invoice!"
            
            p=Process(
                target=SendMail.send_email,
                args=(
                    subject,
                    rendered_template,
                    self.to,
                    True
                )
            )
            p.start()
            return invoice_path,invoice
        except Exception as e:
            raise Exception(str(e))