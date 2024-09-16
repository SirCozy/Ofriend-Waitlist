from django.urls import path
from . import views

urlpatterns = [
    path('course-registration/', views.course_registration_view, name='course_registration'),
]
