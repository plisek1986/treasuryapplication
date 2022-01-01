from django.urls import path
from .views import AccountListView, AccountCreateView, AccountEditView, account_delete


app_name = 'Accounts'


urlpatterns = [
    path('account_list/', AccountListView.as_view(), name='account-list'),
    path('account_create/', AccountCreateView.as_view(), name='account-create'),
    path('account_edit/<int:pk>/', AccountEditView.as_view(), name='account-edit'),
    path('account_delete/<int:pk>/', account_delete, name='account-delete'),
]