from django.shortcuts import render, redirect
from .forms import CourseRegistrationForm

def course_registration_view(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful submission
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration.html', {'form': form})
