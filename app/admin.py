from django.contrib import admin
from .models import (SystemAdmin,OTP,Organization,Employee,Role,PaymentMode,
                     Customer,Product,Order,Billing,AccessLog,ErrorLog,
                     TwoFactorVerification,ProductType,OrderMapToBilling)

admin.site.register(SystemAdmin)
admin.site.register(OTP)
admin.site.register(TwoFactorVerification)
admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(PaymentMode)
admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Billing)
admin.site.register(OrderMapToBilling)
admin.site.register(AccessLog)
admin.site.register(ErrorLog)
