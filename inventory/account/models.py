from django.db import models

# class Profile(models.Model):
#     GENDER = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('others', 'Others'),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(
#         upload_to='profiles', max_length=250, default='profiles/default.jpg')
#     contact = models.CharField(max_length=50, blank=True)
#     gender = models.CharField(choices=GENDER, max_length=250, blank=True)
    
    
#     def __str__(self):
#         return self.user.username
