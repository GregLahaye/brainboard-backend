from django.contrib.auth.models import User
from rest_framework import serializers

from boards.models import Note


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        required=False, many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'notes']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user
