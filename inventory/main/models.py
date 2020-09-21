from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=120)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class CompanyOrder(models.Model):
    STATUS_CHOICE = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
    )
    company_manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name
