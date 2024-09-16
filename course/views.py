from django.shortcuts import render, redirect
from .forms import CourseRegistrationForm
from rest_framework.views import APIView
from rest_framework.response import Response
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
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
