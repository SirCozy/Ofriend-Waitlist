from django.urls import path
from . import views
from .views import ContactListCreate

urlpatterns = [
    path('course-registration/', views.course_registration_view, name='course_registration'),
    path('contacts/', ContactListCreate.as_view(), name='contact-list-create'),
]
