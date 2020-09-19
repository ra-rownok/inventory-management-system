from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



#Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!! You have become an author')
            user = form.save()
           
    else:
        form = SignUpForm()
    return render(request,'account/signup.html', {'form':form} )


#Login
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged Successfully!!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request,'account/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')


#Logout
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')

    





