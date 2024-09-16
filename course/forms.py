from django import forms
from .models import CourseRegistration

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ['name', 'email', 'course_name']
