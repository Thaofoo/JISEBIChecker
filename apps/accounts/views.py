from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import urls

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('loggedHomepage')
        else:
            return HttpResponse("salah kon nglebokno")

    return render(request, "accounts/login.html")


def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("passwormu bedo")
        else:
            user_manu = User.objects.create_user(uname, email, pass1)
            user_manu.save()

            return redirect('login')

    return render(request, "accounts/register.html")
