from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True)
    contacts = models.CharField(max_length=60, blank=False)
    message = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name