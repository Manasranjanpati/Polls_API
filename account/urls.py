from django.urls import path,include,re_path
from django.contrib import admin
from.views import (AccountList,AccountUpdate,AccountDelete,AccountDetail,
AccountCreate)



urlpatterns = [
        path('', AccountList.as_view(), name='account'),
        path('detail/<int:id>', AccountDetail.as_view(), name='detail'),
        path('edit/<int:id>', AccountUpdate.as_view(), name='edit'),
        path('delete/<int:id>', AccountDelete.as_view(), name='delete'),
        path('create/', AccountCreate.as_view(), name='create'),

]