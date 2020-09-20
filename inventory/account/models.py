from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    contact = models.CharField(max_length=50, blank=True)
    gender = models.CharField(choices=GENDER, max_length=250, blank=True)
    profession = models.CharField(max_length=50, blank=True)
   

    def __str__(self):
        return self.user.username
