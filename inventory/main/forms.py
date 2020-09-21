from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from main.models import *

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'quantity', 'price']


class OrderForm(forms.ModelForm):
	class Meta:
		model = CompanyOrder
		fields = ['quantity','status']