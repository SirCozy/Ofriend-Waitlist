from django.urls import path
from .views import create_contact

urlpatterns = [
    path('contacts/', create_contact, name='create_contact'),
]
