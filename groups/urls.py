from django.urls import path
from .views import GroupListCreate

urlpatterns = [
      path('groups/', GroupListCreate.as_view(), name='group-list-create'),
]