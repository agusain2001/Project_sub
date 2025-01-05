from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
     class Meta:
         model = Expense
         fields = ['id', 'amount', 'category', 'split_type', 'date', 'receipt_image', 'participants','created_by', 'group']
         # fields = '__all__' # Use this to include all the fields