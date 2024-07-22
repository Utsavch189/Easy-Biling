from django.contrib import admin
from .models import (SystemAdmin,OTP,Organization,Employee,Role,PaymentMode,
                     Customer,Product,Order,Billing,AccessLog,ErrorLog,
                     TwoFactorVerification,ProductType,OrderMapToBilling,GSTRates)

class BillingAdmin(admin.ModelAdmin):
    list_display=('bill_id','invoice')
    def get_queryset(self, request):
        return Billing.admin_objects.all()

class OrganizationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Organization.admin_objects.all()

class EmployeeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Employee.admin_objects.all()

class RoleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Role.admin_objects.all()

class PaymentModeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return PaymentMode.admin_objects.all()

class CustomerModeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Customer.admin_objects.all()

class ProductTypeModeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return ProductType.admin_objects.all()

class ProductModeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Product.admin_objects.all()

class OrderModeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Order.admin_objects.all()

admin.site.register(SystemAdmin)
admin.site.register(OTP)
admin.site.register(TwoFactorVerification)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(PaymentMode,PaymentModeAdmin)
admin.site.register(Customer,CustomerModeAdmin)
admin.site.register(ProductType,ProductTypeModeAdmin)
admin.site.register(Product,ProductModeAdmin)
admin.site.register(Order,OrderModeAdmin)
admin.site.register(Billing,BillingAdmin)
admin.site.register(GSTRates)
admin.site.register(OrderMapToBilling)
admin.site.register(AccessLog)
admin.site.register(ErrorLog)
