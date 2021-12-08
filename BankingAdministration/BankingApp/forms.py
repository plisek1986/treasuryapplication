from django.forms import ModelForm
from BankingApp.models import User
from django.forms import Form
from django import forms


# class UserCreateForm(ModelForm):
#     """ Class utilizes ModelForm for creating a form for a new user"""
#
#
#     class Meta:
#         """ Class utilizes model User for translating user model attributes into form fields"""
#
#         model = User
#         fields = ['is_superuser', 'first_name', 'last_name', 'email', 'internal_id', 'is_administrator', 'is_payment_creator',
#                   'is_payment_approver', 'can_delete_payment']
from django.utils.safestring import mark_safe


class UserCreateForm(forms.Form):
    is_superuser = forms.BooleanField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailInput()
    internal_id = forms.CharField(max_length=7)
    is_administrator = forms.BooleanField()
    is_payment_creator = forms.BooleanField()
    is_payment_approver = forms.BooleanField()
    can_delete_payment = forms.BooleanField()

