from django import forms
from myapp.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'other_fields']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists.")
        return email
