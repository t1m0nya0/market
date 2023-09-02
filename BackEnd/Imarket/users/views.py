import random
import string
import time

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User

from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from rest_framework.response import Response

random.seed(time.time())


@csrf_exempt
def send_to_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        send_mail(
            subject='Verification',
            message=f'Verification code for registration : {RegisterView.random_gen_code}',
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=[email, ],
            fail_silently=False
        )

    return render(request, 'index.html')


class RegisterView(APIView):
    random_gen_code = ''.join(random.choice(string.digits) for i in range(6))

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.data["user_type"] == "Customer":
            new_order = Order(user=User.objects.get(id=serializer.data["id"]))
            new_order.save()

        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
