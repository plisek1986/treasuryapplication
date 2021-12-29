from django.urls import path
from .views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView

app_name = 'Companies'

urlpatterns = [
    path('company_list/', CompanyListView.as_view(), name='company-list'),
    path('company_create/', CompanyCreateView.as_view(), name='company-create'),
    path('company_create/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company_edit/<int:pk>/', CompanyUpdateView.as_view(), name='company-edit'),
    path('company_delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),
]
