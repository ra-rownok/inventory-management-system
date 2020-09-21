from django.contrib import admin
from django.urls import path
from main import views as main_views
from account import views as account_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='home'),
    path('update/', account_views.update_profile, name='update'),
    path('register/',account_views.register,name='register'),
    path('login/',account_views.login,name='login'),
    path('logout/',account_views.logout,name='logout'),
    path('product/',main_views.product,name='product'),
    path('order/<int:pk>/',main_views.order,name='order'),
    path('vendor/',main_views.vendor,name='vendorlist'),
    # path('orderlist/',main_views.order_list,name='orderlist'),
]