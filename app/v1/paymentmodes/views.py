from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import PaymentMode
from utils import exceptions
from app.serializers.payment_modes import PaymentModeOutSerializer

class PaymentModeView(APIView):

    @is_authorize(role=['ADMIN','MANAGER'])
    def get(self,request):
        token_data=request.token_data
        paymentmodes=PaymentMode.objects.filter(organization__org_id=token_data.get('org_id'))
        data=PaymentModeOutSerializer(instance=paymentmodes,many=True).data
        return Response({"paymentmodes":data,"total":paymentmodes.count()},status=status.HTTP_200_OK)