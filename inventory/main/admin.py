from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(CompanyManager)
admin.site.register(Product)
admin.site.register(VendorOrder)
admin.site.register(CompanyOrder)