from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from account.models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profession', 'gender', 'contact', 'address']
