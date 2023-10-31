from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    department = models.CharField(max_length=255)
    start_date = models.DateField()
    is_onboarded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
