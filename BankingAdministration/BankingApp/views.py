from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views import View
from BankingApp.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


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
        # authentication based on the credentials provided by the user trying to log in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # user will be logged in and his/her ID will be saved in the session
            login(request, user)
            return redirect('dashboard')
        else:
            message = 'Provided credentials are incorrect, please try again.'
            return render(request, 'login.html', context={'message': message})


# login url is provided in the settings as LOGIN_URL, therefore there is no need to provide it as an optional parameter
# in login_required below
@login_required
def dashboard_view(request, *args, **kwargs):
    return render(request, 'dashboard.html')


def log_out(request):
    # in case you would like to display the username who has been logged out (not recommended for security reasons)
    logged_in_user = request.user
    logout(request)
    # Line below returns message to the user with successful log out.
    # request.session['message'] = f'You have been successfully logged out {logged_in_user.username}.'
    # request.session['message'] = f'You have been successfully logged out.'
    return redirect('main_page')


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


