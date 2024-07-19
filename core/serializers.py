from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

class GetUserSerializer(UserSerializer):

    group_name = serializers.SerializerMethodField('get_group')
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'group_name']

    def get_group(self, user=models.User):
        if user.groups.all():
            return user.groups.all()[0].name
        else:
            return ''
        
class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']