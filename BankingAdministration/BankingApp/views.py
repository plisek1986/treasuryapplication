from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
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

#
# class UserListView(ListView):
#     model = User
#     template_name = 'user_list.html'
#
#
# class UserCreateView(View):
#     """View lists user creation fields and includes necessary validations."""
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'user_create.html')
#
#     def post(self, request, *args, **kwargs):
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         if len(username) < 7:
#             message = 'Provided username is too short. Is should consist of 7 characters.'
#             return render(request, 'user_create.html', {'message': message})
#         elif User.objects.filter(username=username):
#             message = 'Provided username already exists in the database'
#             return render(request, 'user_create.html', {'message': message})
#         superuser = request.POST.get('superuser')
#         if superuser == "on":
#             superuser = True
#         else:
#             superuser = False
#         payment_creator = request.POST.get('payment_creator')
#         if payment_creator == "on":
#             payment_creator = True
#         else:
#             payment_creator = False
#         payment_approver = request.POST.get('payment_approver')
#         if payment_approver == "on":
#             payment_approver = True
#         else:
#             payment_approver = False
#         delete_payment = request.POST.get('payment_delete')
#         if delete_payment == "on":
#             delete_payment = True
#         else:
#             delete_payment = False
#         if payment_creator is True and payment_approver is True:
#             message = 'Violation of segregation of duties. User cannot create and approve payments.'
#             return render(request, 'user_create.html', {'message': message})
#         User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
#                             is_superuser=superuser, is_payment_creator=payment_creator,
#                             is_payment_approver=payment_approver, can_delete_payment=delete_payment)
#         return redirect('/user_list/')
#
#
# def user_delete(request, user_id, *args, **kwargs):
#     """
#     Function for deleting user with confirming intention to remove the user.
#     :param request: used by Django to pass state through the system
#     :param user_id: user to be deleted
#     :return: User deleted and administrator redirected to the user list
#     """
#     user = User.objects.get(pk=user_id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('user-list')
#     return render(request, 'user_delete.html', {'user': user})
