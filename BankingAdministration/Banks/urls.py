from django.urls import path
from .views import BankListView, BankCreateView, BankUpdateView, BankDeleteView, BankDetailView

app_name = 'Banks'

urlpatterns = [
    path('bank_list/', BankListView.as_view(), name='bank-list'),
    path('bank_create/', BankCreateView.as_view(), name='bank-create'),
    path('bank_detail/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),
    path('bank_edit/<int:pk>/', BankUpdateView.as_view(), name='bank-edit'),
    path('bank_delete/<int:pk>/', BankDeleteView.as_view(), name='bank-delete'),
]