from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from .models import Bank


class BankListView(LoginRequiredMixin, ListView):
    """View for enlisting all banks available in the database."""

    model = Bank
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BankCreateView(CreateView):
    """
    View for adding a new bank where administrator can define names for new banks.
    Additional validation for existence of a new bank in the database takes place.
    """

    model = Bank
    fields = ['name']


class BankUpdateView(UpdateView):
    """View for editing bank's details. Validation of the existence of the bank in the database takes place. """

    model = Bank
    fields = ['name']
    template_name_suffix = '_update_form'


class BankDeleteView(DeleteView):
    model = Bank
    success_url = reverse_lazy('Banks:bank-list')


class BankDetailView(DetailView):
    """View for displaying all details of a bank, incl. it's accounts."""

    model = Bank


