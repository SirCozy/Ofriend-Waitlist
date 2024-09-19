from django.db import models

class CourseRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
