from django.urls import path
from .views import course_registration_view, thank_you_view

urlpatterns = [
    path('course-registration/', course_registration_view, name='course_registration'),
    path('thank-you/', thank_you_view, name='thank_you'),  
]
