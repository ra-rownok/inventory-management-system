from django.contrib import admin
from django.urls import path
from main import views as main_views
from account import views as account_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='home'),
    
    path('signup/', account_views.signup, name='signup'),
    path('login/', account_views.login, name='login'),
    # path('logout/', account_views.user_logout, name='logout'),
    # path('logout/', account_views.logout, name='logout'),
    # path('profile/', account_views.profile, name='profile'),
    # path('editprofile/', account_views.editprofile, name='editprofile'),
    # path('editpassword/', account_views.editpassword, name='editpassword'),
]
