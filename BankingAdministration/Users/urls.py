from django.urls import path
from .views import UserListView, UserCreateView, user_delete


app_name = 'Users'


urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('user_create/', UserCreateView.as_view(), name='user-create'),
    path('user_delete/<int:user_id>', user_delete, name='user-delete'),
]