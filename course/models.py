from django.db import models

class CourseRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
