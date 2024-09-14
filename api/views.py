from django.shortcuts import render

from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
def register_user_view(request):
    # Your registration logic here


from django.core.exceptions import ValidationError
from myapp.models import User

def register_user(email, other_data):
    if User.objects.filter(email=email).exists():
        raise ValidationError("User with this email already exists.")
    # Proceed to create and save the user


# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer

@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, force_bytes
from django.contrib.sites.shortcuts import get_current_site

def send_verification_email(user, request):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
    activation_link = f"http://{domain}{link}"

    send_mail(
        'Activate Your Account',
        f'Click the following link to activate your account: {activation_link}',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
