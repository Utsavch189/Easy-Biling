from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.otp import OTPSender
from app.models import Employee
from utils import exceptions

class OTPSendView(APIView):

    def post(self,request):
        data=request.data
        email=data.get("email",None)
        user_type=data.get('user_type',None)

        if user_type.lower()=="employee":

            try:
                user=Employee.objects.get(email=email)
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="No user found!")

        OTPSender.send(
            to=email,
            user_id=user.emp_id,
            name=user.name
        )

        return Response({"message":"OTP send!"},status=status.HTTP_200_OK)

        
class OTPVerifyView(APIView):

    def post(self,request):
        data=request.data
        email=data.get("email",None)
        otp=data.get("otp",None)
        user_type=data.get('user_type',None)

        if user_type.lower()=="employee":

            try:
                user=Employee.objects.get(email=email)
            except Employee.DoesNotExist:
                raise exceptions.NotExists(detail="No user found!")
            
            user_id=user.emp_id

        sts,message=OTPSender.verify(
            user_id,
            otp
        )
        if not sts:
            return Response({"message":message,"verified":False},status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message":message,"verified":True},status=status.HTTP_200_OK)


