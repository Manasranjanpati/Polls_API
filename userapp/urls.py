from django.urls import path,include,re_path
from django.contrib import admin
from.views import UserListAPI,UserDetailAPI,UserCreateAPI,UserUpdateAPI,UserDeleteAPI



urlpatterns = [
        path('', UserListAPI.as_view(), name='User'),
        path('detail/<int:id>/', UserDetailAPI.as_view(), name='detail'),
        path('edit/<int:id>/', UserUpdateAPI.as_view(), name='edit'),
        path('delete/<int:id>/', UserDeleteAPI.as_view(), name='delete'),
        path('create/', UserCreateAPI.as_view(), name='create'),

]
