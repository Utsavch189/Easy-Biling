from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.decorators.authorize import is_authorize
from app.models import Customer,Employee
from app.serializers.customer import CustomerOutSerializer
from app.serializers.employee import EmployeeOutSerializer
from utils import exceptions

class MeView(APIView):

    @is_authorize()
    def get(self,request):
        token_data=request.token_data
        user_id=token_data.get('user_id')

        if Employee.objects.filter(emp_id=user_id).exists():
            employee=Employee.objects.get(emp_id=user_id)
            data=EmployeeOutSerializer(instance=employee,many=False).data

        elif Customer.objects.filter(cust_id=user_id).exists():
            customer=Customer.objects.get(cust_id=user_id)
            data=CustomerOutSerializer(instance=customer,many=False).data
        
        else:
            raise exceptions.NotExists(detail="user not found!")
        
        return Response({"user":data},status=status.HTTP_200_OK)