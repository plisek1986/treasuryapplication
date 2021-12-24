from django.urls import path
from .views import BankListView, BankCreateView, BankUpdateView, bank_delete, BankViewView

app_name = 'Banks'

urlpatterns = [
    path('bank_list/', BankListView.as_view(), name='bank-list'),
    path('bank_create/', BankCreateView.as_view(), name='bank-create'),
    path('bank_view/', BankViewView.as_view(), name='bank-view'),
    path('bank_edit/<int:pk>/', BankUpdateView.as_view(), name='bank-edit'),
    path('bank_delete/<int:bank_id>/', bank_delete, name='bank-delete'),

]