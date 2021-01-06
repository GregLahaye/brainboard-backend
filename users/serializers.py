from django.contrib.auth.models import User
from rest_framework import serializers

from boards.models import Board


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(
        required=False, many=True, queryset=Board.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'boards']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user
