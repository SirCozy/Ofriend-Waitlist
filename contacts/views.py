from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
 
 # contacts/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure this template exists
