from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Company, Bank, COUNTRY_CHOICE
from django.http import HttpResponse

IBAN_COUNTRY_CODE_LENGTH = {
    'AT': 20,  # Austria
    'BE': 16,  # Belgium
    'BG': 22,  # Bulgaria
    'CH': 21,  # Switzerland
    'CZ': 24,  # Czech Republic
    'DE': 22,  # Germany
    'DK': 18,  # Denmark
    'EE': 20,  # Estonia
    'ES': 24,  # Spain
    'FI': 18,  # Finland
    'FR': 27,  # France
    'GB': 22,  # United Kingdom
    'GR': 27,  # Greece
    'HR': 21,  # Croatia
    'HU': 28,  # Hungary
    'IE': 22,  # Ireland
    'IS': 26,  # Iceland
    'IT': 27,  # Italy
    'KZ': 20,  # Kazakhstan
    'LT': 20,  # Lithuania
    'LV': 21,  # Latvia
    'NL': 18,  # Netherlands
    'NO': 15,  # Norway
    'PL': 28,  # Poland
    'PT': 25,  # Portugal
    'RO': 24,  # Romania
    'SE': 24,  # Sweden
    'SI': 19,  # Slovenia
    'SK': 24,  # Slovakia
    'TR': 26,  # Turkey
}

# variable utilized in the password creation / validation view
special_characters = '!@#$%^&*()_+-={}[]|:";<>?,./"'


class AccountListView(View):
    """View for enlisting all accounts in the database."""

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all().order_by('-company')
        companies = Company.objects.all()
        return render(request, 'account_list.html', {'accounts': accounts, 'companies': companies})


class AccountCreateView(View):
    """
    View for creating a new account where all account model attributes are enlisted.
    Additional validations of iban number take place in this view.
    """

    def get(self, request, *args, **kwargs):
        banks = Bank.objects.all()
        companies = Company.objects.all()
        country_codes = []
        for country in COUNTRY_CHOICE:
            country_codes.append(country[1])
        return render(request, 'account_create.html', {'banks': banks, 'companies': companies,
                                                       'country_codes': country_codes})

    def post(self, request, *args, **kwargs):
        banks = Bank.objects.all()
        companies = Company.objects.all()
        country_codes = []
        for country in COUNTRY_CHOICE:
            country_codes.append(country[1])
        iban_country_code = request.POST.get('iban1')
        iban_number = request.POST.get('iban2')
        iban_length = len(iban_country_code) + len(iban_number)
        full_iban = iban_country_code + iban_number
        if not iban_number:
            message = 'Please provide iban number.'
            return render(request, 'account_create.html', {'banks': banks, 'companies': companies, 'message': message,
                                                           'country_codes': country_codes})
        elif iban_country_code in IBAN_COUNTRY_CODE_LENGTH and iban_length != \
                IBAN_COUNTRY_CODE_LENGTH[iban_country_code]:
            message = f'Provided iban number is incorrect. Make sure iban has  \
                      {IBAN_COUNTRY_CODE_LENGTH[iban_country_code]} characters'
            return render(request, 'account_create.html', {'banks': banks, 'companies': companies, 'message': message,
                                                           'country_codes': country_codes})
        else:
            if Account.objects.filter(iban_number=full_iban):
                message = 'Provided iban already exists in the database.'
                return render(request, 'account_create.html',
                              {'banks': banks, 'companies': companies, 'message': message,
                               'country_codes': country_codes})

        swift_code = request.POST.get('swift')
        if len(swift_code) > 11:
            message = 'Provided swift code is too long, swift can have maximum of 11 characters'
            return render(request, 'account_create.html', {'banks': banks, 'companies': companies, 'message': message,
                                                           'country_codes': country_codes})
        bank = request.POST.get('bank')
        bank = Bank.objects.get(name=bank)
        company = request.POST.get('company')
        company = Company.objects.get(name=company)
        Account.objects.create(iban_number=full_iban, swift_code=swift_code,
                               bank=bank, company=company)
        return redirect('/Accounts/account_list')


class AccountEditView(View):
    """View for editing account details. Some attributes are not available for the administrator to modify."""

    def get(self, request, account_id, *args, **kwargs):
        # admin = request.session.get('admin_id')
        # if admin is None:
        #     return HttpResponse('You are not authorized')
        # else:
        #     pass
        account = Account.objects.get(pk=account_id)
        return render(request, 'account_edit.html', {'account': account})

    def post(self, request, account_id, *args, **kwargs):
        account = Account.objects.get(pk=account_id)
        iban_number = request.POST.get('iban')
        if not iban_number:
            message = 'Please provide iban number.'
            return render(request, 'account_edit.html', {'account': account, 'message': message})
        elif Account.objects.filter(iban_number=iban_number) and iban_number != account.iban_number:
            message = 'This iban already exists in the database.'
            return render(request, 'account_edit.html', {'account': account, 'message': message})
        else:
            pass
        swift_code = request.POST.get('swift')
        account.iban_number = iban_number
        account.swift_code = swift_code
        account.save()
        return redirect('/Accounts/account_list')


def account_delete(request, account_id, *args, **kwargs):
    """
    Function for deleting an account from the database.
    :param request: used by Django to pass state through the system
    :param account_id: account to be permanently deleted from the database
    :return: administrator is redirected to the account list view
    """

    admin = request.session.get('admin_id')
    if admin is None:
        return HttpResponse('You are not authorized')
    else:
        pass
    account = Account.objects.get(pk=account_id)
    if request.method == 'POST':
        account.delete()
        return redirect('/Accounts/account_list')
    return render(request, 'account_delete.html', {'account': account})
