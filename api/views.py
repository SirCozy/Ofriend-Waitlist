# Views for User Registration with Rate Limiting
from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, force_bytes
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Contact
from .serializers import ContactSerializer
from .forms import CourseRegistrationForm

# Rate limited user registration view (limits to 5 requests per minute by IP)
@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
def register_user_view(request):
    # Registration logic here (e.g., form processing)
    pass

# Register user function with email validation
def register_user(email, other_data):
    if User.objects.filter(email=email).exists():
        raise ValidationError("User with this email already exists.")
    # Proceed to create and save the user here

# API view to create a new contact
@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Sending account activation email
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

# Course registration view
def course_registration_view(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful form submission
    else:
        form = CourseRegistrationForm()

    return render(request, 'course_registration.html', {'form': form})
