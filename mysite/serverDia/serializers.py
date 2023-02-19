from rest_framework import serializers
from .models import DiaUsers


class DiaUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaUsers
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'middle_name',
                  'birth_date', 'weight', 'height', 'attending_doctor', 'app_type', 'last_login', 'is_superuser',
                  'is_staff', 'is_active', 'date_joined']
