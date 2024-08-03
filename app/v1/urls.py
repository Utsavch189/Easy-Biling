from django.urls import path
from app.v1.employee.views import EmployeeView
from app.v1.auths.views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    ForgetPasswordView
)
from app.v1.otp.views import OTPSendView,OTPVerifyView
from app.v1.two_factor_verify.views import TwoFactorCreateView,TwoFactorVerifyView
from app.v1.product.views import ProductView,ProductTypeView
from app.v1.order.views import OrderView
from app.v1.billing.views import BillingView
from app.v1.customer.views import CustomerView
from app.v1.me.views import MeView
from app.v1.paymentmodes.views import PaymentModeView

urlpatterns=[
    path('employee',EmployeeView.as_view()),
    path('auth/register',RegisterView.as_view()),
    path('auth/login',LoginView.as_view()),
    path('auth/refresh-token',RefreshTokenView.as_view()),
    path('auth/forget-password',ForgetPasswordView.as_view()),
    path('otp/send',OTPSendView.as_view()),
    path('otp/verify',OTPVerifyView.as_view()),
    path('2fa/create',TwoFactorCreateView.as_view()),
    path('2fa/verify',TwoFactorVerifyView.as_view()),
    path('product',ProductView.as_view()),
    path('product-type',ProductTypeView.as_view()),
    path('order',OrderView.as_view()),
    path('billing',BillingView.as_view()),
    path('customer',CustomerView.as_view()),
    path('me',MeView.as_view()),
    path('payment-mode',PaymentModeView.as_view())
]