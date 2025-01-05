from django.urls import path
from .views import SettlementListCreate

urlpatterns = [
      path('settlements/', SettlementListCreate.as_view(), name='settlement-list-create'),
]