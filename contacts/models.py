from django.db import models

class Contact(models.Model):
    # define your fields here
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
