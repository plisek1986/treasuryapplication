from django.urls import path
from .views import UserListView, UserCreateView, user_delete, UserView, UserEditView


app_name = 'Users'


urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('user_create/', UserCreateView.as_view(), name='user-create'),
    path('user_view/<int:user_id>', UserView.as_view(), name='user-view'),
    path('user_edit/<int:user_id>', UserEditView.as_view(), name='user-edit'),
    path('user_delete/<int:user_id>', user_delete, name='user-delete'),

]