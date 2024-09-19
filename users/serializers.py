from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()  # This will get the custom user model if it's been replaced

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to handle registration.
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """
        Create and return a new user after saving the hashed password.
        """
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
