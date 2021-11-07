from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from BankingApp.models import User
from django.contrib.auth import authenticate, login


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
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            # user will be logged in and saved in the session
            login(request, user)
            return HttpResponse(f'Jesteś zalogowany jako {user}')
        else:
            return HttpResponse('You are not authorized to loogin!')



