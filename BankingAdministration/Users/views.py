from django.shortcuts import render, redirect
from treasuryapplication.BankingAdministration.BankingApp.models import User
from django.views.generic import ListView
from django.views import View


# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserCreateView(View):
    """View lists user creation fields and includes necessary validations."""

    def get(self, request, *args, **kwargs):
        return render(request, 'user_create.html')

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if len(username) < 7:
            message = 'Provided username is too short. Is should consist of 7 characters.'
            return render(request, 'user_create.html', {'message': message})
        elif User.objects.filter(username=username):
            message = 'Provided username already exists in the database'
            return render(request, 'user_create.html', {'message': message})
        superuser = request.POST.get('superuser')
        if superuser == "on":
            superuser = True
        else:
            superuser = False
        payment_creator = request.POST.get('payment_creator')
        if payment_creator == "on":
            payment_creator = True
        else:
            payment_creator = False
        payment_approver = request.POST.get('payment_approver')
        if payment_approver == "on":
            payment_approver = True
        else:
            payment_approver = False
        delete_payment = request.POST.get('payment_delete')
        if delete_payment == "on":
            delete_payment = True
        else:
            delete_payment = False
        if payment_creator is True and payment_approver is True:
            message = 'Violation of segregation of duties. User cannot create and approve payments.'
            return render(request, 'user_create.html', {'message': message})
        User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                            is_superuser=superuser, is_payment_creator=payment_creator,
                            is_payment_approver=payment_approver, can_delete_payment=delete_payment)
        return redirect('/user_list/')


def user_delete(request, user_id, *args, **kwargs):
    """
    Function for deleting user with confirming intention to remove the user.
    :param request: used by Django to pass state through the system
    :param user_id: user to be deleted
    :return: User deleted and administrator redirected to the user list
    """
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user-list')
    return render(request, 'user_delete.html', {'user': user})
