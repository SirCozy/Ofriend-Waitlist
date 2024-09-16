# contacts/urls.py

from django.urls import path
from .views import ContactListCreate

urlpatterns = [
    path('contact/', ContactListCreate.as_view(), name='contact-list-create'),
]
