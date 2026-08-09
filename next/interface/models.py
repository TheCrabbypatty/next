from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    estimated_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
