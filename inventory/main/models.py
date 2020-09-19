from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CompanyManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class VendorOrder(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

class CompanyOrder(models.Model):
    STATUS_CHOICE = (
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    company_manager = models.ForeignKey(CompanyManager, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=120, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name
