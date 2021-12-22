from django.contrib import admin
from BankingApp.views import MainPageView, LoginView, dashboard_view, log_out
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('log_out/', log_out, name='log_out'),
    path('Users/', include('Users.urls', namespace='Users')),
    path('Accounts/', include('Accounts.urls', namespace='Accounts')),
]

