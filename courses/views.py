from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import CourseRegistrationForm
from .models import Contact
from .serializers import ContactSerializer

def course_registration_view(request: HttpRequest) -> HttpResponse:
    """
    Handle course registration form submission.
    """

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful submission
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration.html', {'form': form})

class ContactListCreate(APIView):
    """
    List all contacts or create a new contact.
    """

    def get(self, request: HttpRequest) -> Response:
        """
        Return a list of all contacts.
        """
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        """
        Create a new contact.
        """
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def thank_you_view(request):
    return render(request, 'thank_you.html')