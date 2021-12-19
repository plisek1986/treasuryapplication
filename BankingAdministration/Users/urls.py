from django.contrib import admin
from django.urls import path
from terasuryapplication.BankingAdministration.Users.views import views as all_views
from django.urls import path, include


app_name = 'users'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_list/', all_views.UserListView.as_view(), name='user_list'),
    path('user_create/', all_views.UserCreateView.as_view(), name='user_create'),
    path('user_delete/<int:user_id>', all_views.user_delete, name='user_delete'),
]