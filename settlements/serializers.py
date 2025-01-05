from rest_framework import serializers
from .models import Settlement


class SettlementSerializer(serializers.ModelSerializer):
     class Meta:
         model = Settlement
         fields = ['id', 'payer', 'payee', 'amount', 'payment_status', 'settlement_method', 'due_date', 'group']
         # fields = '__all__' # Use this to include all the fields