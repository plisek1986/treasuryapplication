from django.urls import path
from .views import BankListView, BankCreateView, BankEditView, bank_delete

app_name = 'Banks'

urlpatterns = [
    path('bank_list/', BankListView.as_view(), name='bank-list'),
    path('bank_create/', BankCreateView.as_view(), name='bank-create'),
    path('bank_edit/', BankEditView.as_view(), name='bank-edit'),
    path('bank_delete', bank_delete, name='bank-delete'),

]