from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignInForm
# Create your views here.


def SignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
        else:
            SignInForm()
    context = {
        'form':form
    }

    return render(request , 'accounts/signin.html' , context)
