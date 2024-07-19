from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.two_factor_auth import TwoFactorOTP,GenerateQr
from app.models import Employee
from utils import exceptions
from datetime import datetime

class TwoFactorCreateView(APIView):

    def post(self,request):
        data=request.data
        user_id=data.get('user_id',None)
        user_type=data.get('user_type',None)

        if user_type.lower()=='employee':

            try:
                employee=Employee.objects.get(emp_id=user_id)
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="User doesn't exists!")
            
            GenerateQr.generate(
                username=employee.name,
                user_id=user_id
            )
        return Response({"message":"qr generated"},status=status.HTTP_200_OK)



class TwoFactorVerifyView(APIView):

    def post(self,request):
        data=request.data
        user_id=data.get('user_id',None)
        user_type=data.get('user_type',None)
        otp=data.get('otp',None)

        if user_type.lower()=='employee':

            try:
                employee=Employee.objects.get(emp_id=user_id)
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="User doesn't exists!")
            
            otp_obj=TwoFactorOTP(user_id)

            if not otp_obj.verify(
                otp=otp
            ):
                return Response({"message":"wrong otp!","verified":False},status=status.HTTP_200_OK)
            
            employee.verified_at=datetime.now()
            employee.save()
            
        return Response({"message":"verified!","verified":True},status=status.HTTP_200_OK)
