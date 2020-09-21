from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    PROFESSION = [
        ('Company Manager', 'Company Manager'),
        ('Vendor', 'Vendor')
    ]
    
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=False)
    profession = models.CharField(choices=PROFESSION, max_length=250, blank=True)
    gender = models.CharField(choices=GENDER, max_length=250, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.user.username