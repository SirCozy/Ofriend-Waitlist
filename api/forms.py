from django import forms
from api.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser  

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']  # Correct fields

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists.")
        return email


class CourseRegistrationForm(forms.Form):
    # Define your form fields here
    course_name = forms.CharField(max_length=100)
    start_date = forms.DateField()
    duration = forms.IntegerField()

