from rest_framework import serializers
from src.models.users import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        exclude = ('password', 'salt',)
