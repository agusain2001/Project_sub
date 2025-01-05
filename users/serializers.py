from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'college', 'semester', 'default_payment_methods']
        # fields = '__all__' # Use this to include all the fields