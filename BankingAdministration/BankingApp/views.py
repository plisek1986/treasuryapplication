from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views import View
from BankingApp.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from BankingApp.forms import UserCreateForm


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


class UserCreateView(View):
    """View lists user creation fields and includes necessary validations."""

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, 'user_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        pass
        # form = UserCreateForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     surname = form.cleaned_data['surname']
        #     internal_id = form.cleaned_data['internal_id']
        #     if len(internal_id) < 7:
        #         message = 'Provided internal ID is too short'
        #         return render(request, 'user_create.html', {'form': form, 'message': message})
        #     elif User.objects.filter(internal_id=internal_id):
        #         message = 'Provided internal ID already exists in the database'
        #         return render(request, 'user_create.html', {'form': form, 'message': message})
        #     is_payment_approver = form.cleaned_data['is_payment_approver']
        #     is_payment_creator = form.cleaned_data['is_payment_creator']
        #     is_administrator = form.cleaned_data['is_administrator']
        #     can_delete_payment = form.cleaned_data['can_delete_payment']
        #     if is_payment_creator is True and is_payment_approver is True:
        #         message = 'Violation of segregation of duties. User cannot create and approve payments.'
        #         return render(request, 'user_create.html', {'form': form, 'message': message})
        #     User.objects.create(name=name, surname=surname, internal_id=internal_id,
        #                         is_administrator=is_administrator, is_payment_creator=is_payment_creator,
        #                         is_payment_approver=is_payment_approver, can_delete_payment=can_delete_payment)
        return redirect('/users_list/')
