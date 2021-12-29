from django.urls import path
from .views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView

app_name = 'Companies'

urlpatterns = [
    path('bank_list/', CompanyListView.as_view(), name='company-list'),
    path('bank_create/', CompanyCreateView.as_view(), name='company-create'),
    path('bank_detail/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('bank_edit/<int:pk>/', CompanyUpdateView.as_view(), name='company-edit'),
    path('bank_delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),
]
