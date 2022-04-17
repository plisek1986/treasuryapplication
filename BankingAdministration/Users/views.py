from django.shortcuts import render, redirect
from .models import User, DEPARTMENT_CHOICE
from django.views.generic import ListView
from django.views import View
from Accounts.models import Account


# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserCreateView(View):
    """View lists user creation fields and includes necessary validations."""

    def get(self, request, *args, **kwargs):

        departments = []
        for department in DEPARTMENT_CHOICE:
            departments.append(department[1])
        return render(request, 'user_create.html', {'departments': departments})

    def post(self, request, *args, **kwargs):

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        departments = []
        for department in DEPARTMENT_CHOICE:
            departments.append(department[1])
        username = request.POST.get('username')
        if len(username) < 7:
            message = 'Provided username is too short. Is should consist of 7 characters.'
            return render(request, 'user_create.html', {'message': message, 'departments': departments})
        elif User.objects.filter(username=username):
            message = 'Provided username already exists in the database'
            return render(request, 'user_create.html', {'message': message, 'departments': departments})
        # payment_creator = request.POST.get('can_create')
        # if payment_creator == "on":
        #     payment_creator = True
        # else:
        #     payment_creator = False
        # payment_approver = request.POST.get('can_approve')
        # if payment_approver == "on":
        #     payment_approver = True
        # else:
        #     payment_approver = False
        # delete_payment = request.POST.get('can_delete')
        # if delete_payment == "on":
        #     delete_payment = True
        # else:
        #     delete_payment = False
        # if payment_creator is True and payment_approver is True:
        #     message = 'Violation of segregation of duties. User cannot create and approve payments.'
        #     return render(request, 'user_create.html', {'message': message})
        # department = request.POST.get('department')
        User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                            department=department)
        # is_payment_creator=payment_creator,
        # is_payment_approver=payment_approver, can_delete_payment=delete_payment)
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
               'department': user.department,
               # 'is_payment_creator': user.is_payment_creator,
               # 'is_payment_approver': user.is_payment_approver,
               # 'can_delete_payment': user.can_delete_payment,
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
        # accounts = Account.objects.all()
        departments = []
        for department in DEPARTMENT_CHOICE:
            if user.department == department[1]:
                pass
            else:
                departments.append(department[1])
        return render(request, 'user_edit.html', {'user': user, 'departments': departments})
        # 'accounts': accounts --> to też ma pójść do ctx

    def post(self, request, user_id, *args, **kwargs):

        user = User.objects.get(pk=user_id)
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        # is_payment_approver = request.POST.get('can_approve')
        # if is_payment_approver == "on":
        #     is_payment_approver = True
        # else:
        #     is_payment_approver = False
        # is_payment_creator = request.POST.get('can_create')
        # if is_payment_creator == "on":
        #     is_payment_creator = True
        # else:
        #     is_payment_creator = False
        # can_delete_payment = request.POST.get('can_delete')
        # if can_delete_payment == "on":
        #     can_delete_payment = True
        # else:
        #     can_delete_payment = False
        # if is_payment_creator is True and is_payment_approver is True:
        #     message = 'Violation of segregation of duties. User cannot create and approve payments.'
        #     return render(request, 'user_edit.html', {'user': user, 'message': message})
        user.last_name = last_name
        user.department = department
        # user.is_payment_creator = is_payment_creator
        # user.is_payment_approver = is_payment_approver
        # user.can_delete_payment = can_delete_payment
        user.save()
        return redirect(f'/Users/user_list/')


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
        return redirect('/Users/user_list')
    return render(request, 'user_delete.html', {'user': user})


# class UserAddAccount(View):
#
#     def get(self, request, user_id, *args, **kwargs):
#
#         user = User.objects.get(pk=user_id)
#         accounts = Account.objects.all()
#         for account in accounts:
#             if user.is_payment_creator == 'on':
#                 is_payment_creator = True
#             else:
#                 is_payment_creator = False
#             if user.is_payment_approver == 'on':
#                 is_payment_approver = True
#             else:
#                 is_payment_approver = False
#             if user.can_delete_payment == 'on':
#                 can_delete = True
#             else:
#                 can_delete = False
#
#             return render(request, 'user_add_accounts.html', {'accounts': accounts,
#                                                               'user': user,
#                                                               'can_create': is_payment_creator,
#                                                               'can_approve': is_payment_approver,
#                                                               'can_delete': can_delete})
#
#     def post(self, request, user_id, *args, **kwargs):
#         user = User.objects.get(pk=user_id)
#         accounts = Account.objects.all()
#         for account in accounts:
#             is_payment_approver = request.POST.get('can_approve')
#             if is_payment_approver == "on":
#                 is_payment_approver = True
#             else:
#                 is_payment_approver = False
#             is_payment_creator = request.POST.get('can_create')
#             if is_payment_creator == "on":
#                 is_payment_creator = True
#             else:
#                 is_payment_creator = False
#             can_delete_payment = request.POST.get('can_delete')
#             if can_delete_payment == "on":
#                 can_delete_payment = True
#             else:
#                 can_delete_payment = False
#             if is_payment_creator is True and is_payment_approver is True:
#                 message = 'Violation of segregation of duties. User cannot create and approve payments.'
#                 return render(request, 'user_add_account.html', {'user': user, 'message': message})
#             account.user.is_payment_creator = is_payment_creator
#             account.user.is_payment_approver = is_payment_approver
#             account.user.can_delete_payment = can_delete_payment
#             account.save()
#             return redirect(f'/Users/user_view/{user_id}')

class UserAddAccountsView(View):
    """
    View for adding new accounts to which the user can have access. Only accounts that user does not have access to yet
    are enlisted in this view.
    """

    def get(self, request, user_id, *args, **kwargs):
        # admin = request.session.get('admin_id')
        # if admin is None:
        #     return HttpResponse('You are not authorized')
        # else:
        #     pass
        user = User.objects.get(pk=user_id)
        accounts = Account.objects.all()
        user_accounts = user.account_set.all()
        available_accounts = []
        for account in accounts:
            if account not in user_accounts:
                available_accounts.append(account)
        return render(request, 'user_add_accounts.html', {'user': user, 'available_accounts': available_accounts})

    def post(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        accounts = Account.objects.all()
        user_accounts = user.account_set.all()
        available_accounts = []
        for account in accounts:
            if account not in user_accounts:
                available_accounts.append(account)
        for account in available_accounts:
            user.is_payment_approver = request.POST.get('can_approve')
            if user.is_payment_approver == "on":
                user.is_payment_approver = True
            else:
                user.is_payment_approver = False
            user.is_payment_creator = request.POST.get('can_create')
            if user.is_payment_creator == "on":
                user.is_payment_creator = True
            else:
                user.is_payment_creator = False
            user.can_delete_payment = request.POST.get('can_delete')
            if user.can_delete_payment == "on":
                user.can_delete_payment = True
            else:
                user.can_delete_payment = False
            if user.is_payment_creator is True and user.is_payment_approver is True:
                message = 'Violation of segregation of duties. User cannot create and approve payments.'
                return render(request, 'user_add_account.html', {'user': user, 'message': message})
            account.user.is_payment_creator = user.is_payment_creator
            account.user.is_payment_approver = user.is_payment_approver
            account.user.can_delete_payment = user.can_delete_payment
            account.save()
            return redirect(f'/Users/user_view/{user_id}')
        accounts = request.POST.getlist('accounts')
        for account in accounts:
            user_account = Account.objects.get(iban_number=account)
            user.account.add(user_account)
        user.save()
        return redirect(f'/user_view/{user_id}/')
