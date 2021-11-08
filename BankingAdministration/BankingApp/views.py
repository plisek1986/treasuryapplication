from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from BankingApp.models import User
from django.contrib.auth import authenticate, login, logout


class MainPageView(View):
    """Brief explanation on the purpose of the page with option to log in"""

    def get(self, request, *args, **kwargs):
        return render(request, 'main_page.html')


class LoginView(View):
    """For user to provide login credentials"""

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # user will be logged in and his/her ID will be saved in the session
            login(request, user)
            return redirect('dashboard')
        else:
            message = 'Provided credentials are incorrect, please try again'
            return render(request, 'login.html', context={'message': message})


class DashboardView(View):
    """Logged in user has access to various functionalities of the platform"""

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')


def log_out(request):
    logout(request)
    return redirect('main_page')