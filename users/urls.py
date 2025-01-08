
from django.urls import path
from .views import UserListCreate, TokenAPI, UserDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('token/', TokenAPI.as_view(), name='get-token'),
]
