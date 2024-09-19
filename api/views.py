from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from .models import Contact
from .serializers import ContactSerializer
from .forms import CourseRegistrationForm

# Get the custom user model
User = get_user_model()

# Rate-limited user registration view (for traditional forms, not API)
@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
def register_user_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        other_data = request.POST.get('other_data')
        try:
            # Ensure `register_user` function is defined elsewhere
            register_user(email, other_data)
            return redirect('thank_you')  # Redirect after successful registration
        except ValidationError as e:
            return render(request, 'register.html', {'error': str(e)})
    return render(request, 'register.html')

# CSRF-exempt API view to create a new contact
@csrf_exempt
@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Send account activation email
def send_verification_email(user, request):
    # Ensure `account_activation_token` is defined elsewhere
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

# Course registration view (for traditional forms)
def course_registration_view(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful form submission
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration.html', {'form': form})

# CSRF-exempt user registration API view
@csrf_exempt
@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required'}, status=400)
    
    try:
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'})
    except Exception as e:
        return JsonResponse({'error': f'Error creating user: {str(e)}'}, status=400)
