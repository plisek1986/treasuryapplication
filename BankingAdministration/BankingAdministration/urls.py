from django.contrib import admin
from django.urls import path
from treasuryapplication.BankingAdministration.BankingApp import views as all_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_views.MainPageView.as_view(), name='main_page'),
    path('login/', all_views.LoginView.as_view(), name='login'),
    path('dashboard/', all_views.dashboard_view, name='dashboard'),
    path('log_out/', all_views.log_out, name='log_out'),
    # path('user_list/', all_views.UserListView.as_view(), name='user_list'),
    # path('user_create/', all_views.UserCreateView.as_view(), name='user_create'),
    # path('user_delete/<int:user_id>', all_views.user_delete, name='user_delete'),
    path('users/', include('users.urls', namespace='users')),
]

