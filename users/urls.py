
from django.urls import path
from .views import UserListCreate, TokenAPI

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('token/', TokenAPI.as_view(), name='get-token'),
]
