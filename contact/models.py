from django.db import models
import uuid

class Message(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self) -> str:
        return self.subject


class Consultation(models.Model):

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)  
    description = models.TextField(max_length=5000, null=True, blank=True)
    current_website = models.URLField(max_length=255, null=True, blank=True) 
    date = models.DateField()
    time = models.TimeField()
    consultation_method = models.CharField(max_length=255, null=True, blank=True)  
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self) -> str:
        return self.email