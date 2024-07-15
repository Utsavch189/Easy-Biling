from django.urls import path
from app.v1.employee.views import EmployeeView,GetAllEmployeeView
from app.v1.auths.views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    ForgetPasswordView
)
from app.v1.otp.views import OTPSendView,OTPVerifyView
from app.v1.two_factor_verify.views import TwoFactorCreateView,TwoFactorVerifyView
from app.v1.product.views import ProductView,ProductTypeView

urlpatterns=[
    path('employee',EmployeeView.as_view()),
    path('employee/get-all',GetAllEmployeeView.as_view()),
    path('auth/register',RegisterView.as_view()),
    path('auth/login',LoginView.as_view()),
    path('auth/refresh-token',RefreshTokenView.as_view()),
    path('auth/forget-password',ForgetPasswordView.as_view()),
    path('otp/send',OTPSendView.as_view()),
    path('otp/verify',OTPVerifyView.as_view()),
    path('2fa/create',TwoFactorCreateView.as_view()),
    path('2fa/verify',TwoFactorVerifyView.as_view()),
    path('product',ProductView.as_view()),
    path('product-type',ProductTypeView.as_view())
]