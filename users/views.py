from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()  # This will get the custom user model if it's been replaced

class RegisterUserView(CreateAPIView):
    """
    API view for registering a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle user registration logic, ensuring valid data and user creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate the data
        user = serializer.save()  # Create the user if data is valid
        return Response(
            {'message': 'User registered successfully!'},
            status=status.HTTP_201_CREATED
        )
