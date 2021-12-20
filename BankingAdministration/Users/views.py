from django.shortcuts import render, redirect
from .models import User
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
        return redirect('/Users/user_list/')


class UserView(View):
    """View displays all details of the user including accounts to which user has access."""

    def get(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        # accounts = user.account.all()
        ctx = {'first_name': user.first_name,
               'last_name': user.last_name,
               'username': user.username,
               'email': user.email,
               'is_superuser': user.is_superuser,
               'is_payment_creator': user.is_payment_creator,
               'is_payment_approver': user.is_payment_approver,
               'can_delete_payment': user.can_delete_payment,
               # 'accounts': accounts,
               }
        return render(request, 'user_view.html', ctx)


class UserEditView(View):
    """
    View where admin can modify details related to the user, including adding or removing accounts
    and access rights.
    """

    def get(self, request, user_id, *args, **kwargs):

        user = User.objects.get(pk=user_id)
        accounts = Account.objects.all()
        return render(request, 'user_edit.html', {'user': user, 'accounts': accounts})

    def post(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        surname = request.POST.get('user_surname')
        is_administrator = request.POST.get('administrator')
        if is_administrator == "on":
            is_administrator = True
        else:
            is_administrator = False
        is_payment_creator = request.POST.get('creator')
        if is_payment_creator == "on":
            is_payment_creator = True
        else:
            is_payment_creator = False
        is_payment_approver = request.POST.get('approver')
        if is_payment_approver == "on":
            is_payment_approver = True
        else:
            is_payment_approver = False
        can_delete_payment = request.POST.get('delete')
        if can_delete_payment == "on":
            can_delete_payment = True
        else:
            can_delete_payment = False
        if is_payment_creator is True and is_payment_approver is True:
            message = 'Violation of segregation of duties. User cannot create and approve payments.'
            return render(request, 'user_edit.html', {'user': user, 'message': message})
        user.surname = surname
        user.is_administrator = is_administrator
        user.is_payment_creator = is_payment_creator
        user.is_payment_approver = is_payment_approver
        user.can_delete_payment = can_delete_payment
        user.save()
        return redirect(f'/user_view/{user_id}/')





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
