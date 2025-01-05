from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
      class Meta:
          model = Category
          fields = ['id', 'name']
          # fields = '__all__' # Use this to include all the fields