from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from .models import Company


class CompanyListView(LoginRequiredMixin, ListView):
    """View for enlisting all banks available in the database."""

    model = Company


class CompanyCreateView(CreateView):
    """
    View for adding a new bank where administrator can define names for new banks.
    Additional validation for existence of a new bank in the database takes place.
    """

    model = Company
    fields = ['name', 'country']
    template_name_suffix = '_create_form'


class CompanyUpdateView(UpdateView):
    """View for editing bank's details. Validation of the existence of the bank in the database takes place. """

    model = Company
    fields = ['name', 'country']
    template_name_suffix = '_update_form'


class CompanyDeleteView(DeleteView):

    model = Company
    success_url = reverse_lazy('Companies:company-list')


class CompanyDetailView(DetailView):
    """View for displaying all details of a bank, incl. it's accounts."""

    model = Company
