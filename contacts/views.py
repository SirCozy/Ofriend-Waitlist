# contacts/views.py

from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Contact
from .serializers import ContactSerializer

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')  # Ensure this template exists

class ContactListCreate(generics.ListCreateAPIView):
    """
    List all contacts or create a new contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    Handle CRUD operations for contacts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
