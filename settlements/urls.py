from django.urls import path
from .views import SettlementListCreate, SettlementDetail

urlpatterns = [
      path('settlements/', SettlementListCreate.as_view(), name='settlement-list-create'),
      path('settlements/<int:pk>', SettlementDetail.as_view(), name='settlement-detail'),
]