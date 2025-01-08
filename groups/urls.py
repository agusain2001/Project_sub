from django.urls import path
from .views import GroupListCreate, GroupDetail

urlpatterns = [
      path('groups/', GroupListCreate.as_view(), name='group-list-create'),
      path('groups/<int:pk>', GroupDetail.as_view(), name='group-detail')
]