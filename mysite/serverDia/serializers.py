from rest_framework import serializers
from .models import DiaUsers


class DiaUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaUsers
        fields = ['id', 'email', 'password', 'name', 'last_name', 'middle_name',
                  'birth_date', 'weigth', 'height', 'attending_doctor', 'app_type']

# class DiaUsersSerializer(serializers.Serializer):
#     id = serializers.IntegerField(primary_key=True, unique=True)
#     email = serializers.CharField(unique=True, max_length=80)
#     password = serializers.CharField(max_length=80)
#     name = serializers.CharField(max_length=80)
#     last_name = serializers.CharField(max_length=80)
#     middle_name = serializers.CharField(max_length=80)
#     birth_date = serializers.DateField()
#     weight = serializers.FloatField()
#     height = serializers.FloatField()
#     attending_doctor = serializers.CharField(max_length=80)
#     app_type = serializers.CharField(max_length=80)
#
#     def create(self, validated_data):
#         return DiaUsers()
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.name = validated_data.get('name', instance.name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.middle_name = validated_data.get('middle_name', instance.middle_name)
#         instance.birth_date = validated_data.get('birth_date', instance.birth_date)
#         instance.weight = validated_data.get('weight', instance.weight)
#         instance.height = validated_data.get('height', instance.height)
#         instance.attending_doctor = validated_data.get('attending_doctor', instance.attending_doctor)
#         instance.app_type = validated_data.get('app_type', instance.app_type)
#         instance.save()
#         return instance
