from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()  # This will get the custom user model if it's been replaced

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to handle registration.
    """
    class Meta:
        model = User
        fields = ['username', 'email']  # Removed 'password'

    def create(self, validated_data):
        """
        Create and return a new user without a password.
        """
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.save()  # No password handling needed
        return user
