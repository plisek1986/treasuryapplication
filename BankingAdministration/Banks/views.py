from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import UpdateView
from .models import Bank
from django.http import HttpRequest, HttpResponse, Http404
from .forms import BankCreateForm, BankUpdateForm
from django.urls import reverse_lazy


class BankListView(ListView):
    """View for enlisting all banks available in the database."""

    model = Bank
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BankCreateView(View):
    """
    View for adding a new bank where administrator can define names for new banks.
    Additional validation for existence of a new bank in the database takes place.
    """

    # def get(self, request, *args, **kwargs):
    #     form = BankCreateForm()
    #     return render(request, 'bank_create.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = BankCreateForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         if Bank.objects.filter(name=name):
    #             message = 'This bank already exists in database.'
    #             return render(request, 'bank_create.html', {'form': form, 'message': message})
    #         Bank.objects.create(name=name)
    #         return redirect('/Banks/bank_list')


class BankUpdateView(UpdateView):
    """View for editing bank's details. Validation of the existence of the bank in the database takes place. """

    model = Bank
    fields = ['name']
    template_name_suffix = '_update_form'


def bank_delete(request, bank_id, *args, **kwargs):
    """
    Function for deleting bank from the database. All accounts associated with this bank are also deleted from the database.
    :param request: used by Django to pass state through the system
    :param bank_id: bank to be deleted from the database
    :return: administrator is redirected to the list of banks
    """

    bank = Bank.objects.get(pk=bank_id)
    if request.method == 'POST':
        bank.delete()
        return redirect('/Banks/bank_list')
    return render(request, 'bank_delete.html', {'bank': bank})


class BankViewView(View):
    """View for displaying all details of a bank, incl. it's accounts."""

    def get(self, request, bank_id):
        bank = Bank.objects.get(pk=bank_id)
        accounts = bank.account_set.all()
        return render(request, 'bank_view.html', {'bank': bank, 'accounts': accounts})
