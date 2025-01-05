from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
     class Meta:
         model = Group
         fields = ['id', 'name', 'group_type', 'members', 'created_by']
         # fields = '__all__' # Use this to include all the fields