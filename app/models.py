from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
from utils import exceptions

class OTP(models.Model):
    user_id=models.CharField(max_length=255,unique=True)
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(default=datetime.now())
    will_expire_at=models.DateTimeField(default=datetime.now())

class TwoFactorVerification(models.Model):
    user_id=models.CharField(max_length=255,unique=True)
    qr_path=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now())

class Organization(models.Model):
    org_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=100,null=True,blank=True)
    registered_at=models.DateTimeField(default=datetime.now())
    is_active=models.BooleanField(default=1)
    updated_at=models.DateTimeField(null=True,blank=True)


    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Organization, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    role_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=50)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_roles',null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())
    is_active=models.BooleanField(default=1)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Role, self).save(*args, **kwargs)

class PaymentMode(models.Model):
    mode_id=models.CharField(max_length=255,unique=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_payment_modes')
    name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=1)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(PaymentMode, self).save(*args, **kwargs)

class SystemAdmin(models.Model):
    admin_id=models.CharField(max_length=255,unique=True)
    password=models.TextField()
    role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name='system_role')

    def __str__(self) -> str:
        return self.admin_id
    

class Employee(models.Model):
    emp_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_employee')
    role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name='employee_role')
    mobile=models.CharField(max_length=20,unique=True)
    email=models.EmailField(max_length=100,null=True,blank=True,unique=True)
    password=models.TextField()
    registered_at=models.DateTimeField(default=datetime.now())
    verified_at=models.DateTimeField(null=True,blank=True)
    is_active=models.BooleanField(default=1)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def is_correct_password(self, password: str):
        return check_password(password, self.password)
    
    def clean(self) -> None:
        if self.email and Employee.objects.filter(email=self.email).exists() and Employee.objects.get(email=self.email).emp_id!=self.emp_id:
            raise exceptions.GenericException(detail="email already exists!",code=400)
        
        if self.mobile and Employee.objects.filter(mobile=self.mobile).exists() and Employee.objects.get(mobile=self.mobile).emp_id!=self.emp_id:
            raise exceptions.GenericException(detail="mobile number already exists!",code=400)
    
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        if not self.id:
            self.password=make_password(self.password)
        self.full_clean()
        super(Employee, self).save(*args, **kwargs)

class Customer(models.Model):
    cust_id=models.CharField(max_length=255,unique=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_customer')
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True,default="")
    registered_at=models.DateTimeField(default=datetime.now())
    is_active=models.BooleanField(default=1)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Customer, self).save(*args, **kwargs)

class ProductType(models.Model):
    p_type_id=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_product_type',default=0)
    desc=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=1)
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(null=True,blank=True)

    def clean(self) -> None:
        if self.name and ProductType.objects.filter(name=self.name).exists() and ProductType.objects.get(name=self.name).p_type_id!=self.p_type_id:
            raise exceptions.GenericException(detail="product type already exists!",code=400)

    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        self.full_clean()
        super(ProductType, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    p_id=models.CharField(max_length=255,unique=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_product')
    name=models.CharField(max_length=255)
    types=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='product_type',null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=10, decimal_places=2,default=0,null=True,blank=True)
    is_available=models.BooleanField(default=1)
    is_active=models.BooleanField(default=1)
    added_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def clean(self) -> None:
        if self.name and Product.objects.filter(name=self.name).exists() and Product.objects.get(name=self.name).p_id!=self.p_id:
            raise exceptions.GenericException(detail="product already exists!",code=400)
    
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        self.full_clean()
        super(Product, self).save(*args, **kwargs)

class Order(models.Model):
    order_id=models.CharField(max_length=255,unique=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_order')
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,related_name='customer_order')
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name='product_order')
    quantity=models.IntegerField()
    order_date=models.DateTimeField(default=datetime.now())
    is_active=models.BooleanField(default=1)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return f"Product : {self.product.name} for Customer : {self.customer.name}"

class GSTRates(models.Model):
    cgst=models.DecimalField(max_digits=10, decimal_places=2)
    sgst=models.DecimalField(max_digits=10, decimal_places=2)
    igst=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"cgst : {self.cgst} , sgst : {self.sgst} , igst : {self.igst}"

class Billing(models.Model):
    bill_id=models.CharField(max_length=255,unique=True)
    invoice=models.CharField(max_length=255,default="")
    invoice_path=models.CharField(max_length=255,default="")
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='organization_billing')
    billed_by=models.ForeignKey(Employee,on_delete=models.DO_NOTHING,related_name='employee_billing')
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,related_name='customer_billing')
    payment_mode=models.ForeignKey(PaymentMode,on_delete=models.DO_NOTHING,related_name='paymode_billing')
    discount=models.DecimalField(max_digits=10, decimal_places=2,default=0,null=True,blank=True)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price=models.DecimalField(max_digits=10, decimal_places=2,default=0,null=True,blank=True)
    cgst_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    sgst_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    igst_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    cgst_rates=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    sgst_rates=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    igst_rates=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_inter_state = models.BooleanField(default=False, help_text="Is this an inter-state transaction?")
    taxable_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    billing_date=models.DateTimeField(default=datetime.now())
    is_active=models.BooleanField(default=1)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return f"Billing For : {self.customer.name} at : {self.billing_date}"

class OrderMapToBilling(models.Model):
    order=models.ForeignKey(Order,on_delete=models.DO_NOTHING,related_name='order_mapping')
    billing=models.ForeignKey(Billing,on_delete=models.CASCADE,related_name='billing_mapping')
    

class ErrorLog(models.Model):
    uid = models.CharField(max_length=255, primary_key=True)
    error_message=models.TextField()
    user_id=models.CharField(max_length=255,null=True,blank=True)
    user_type=models.CharField(max_length=255,null=True,blank=True)
    request_method=models.CharField(max_length=255,null=True,blank=True)
    request_headers=models.TextField(null=True,blank=True)
    request_parameters=models.CharField(max_length=255,null=True,blank=True)
    request_body=models.TextField(null=True,blank=True)
    client_ip=models.CharField(max_length=255,null=True,blank=True)
    stack_trace=models.TextField()
    exception_type=models.CharField(max_length=255,null=True,blank=True)
    view_name=models.CharField(max_length=255,null=True,blank=True)
    response_status_code=models.CharField(max_length=255,null=True,blank=True)
    enviroment=models.CharField(max_length=255,null=True,blank=True)
    error_location=models.CharField(max_length=255,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())
    
    def __str__(self) -> str:
        return f"Error : {self.response_status_code} at {self.created_at}"

class AccessLog(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    request_method = models.CharField(max_length=255, null=True, blank=True)
    request_headers = models.TextField(null=True, blank=True)
    request_parameters = models.CharField(max_length=255, null=True, blank=True)
    request_body = models.TextField(null=True, blank=True)
    client_ip = models.CharField(max_length=255, null=True, blank=True)
    view_name = models.CharField(max_length=255, null=True, blank=True)
    response_status_code = models.CharField(max_length=255, null=True, blank=True)
    environment = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    response_content = models.TextField(null=True, blank=True)
    request_url = models.URLField(max_length=2000, null=True, blank=True)
    user_agent = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    referer = models.URLField(max_length=2000, null=True, blank=True)
    request_query_params = models.JSONField(null=True, blank=True)
    response_headers = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Log: {self.response_status_code} at {self.created_at} method {self.request_method} url {self.request_url}"