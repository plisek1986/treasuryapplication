from django.forms import ModelForm
from .models import Bank


class BankCreateForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name']
