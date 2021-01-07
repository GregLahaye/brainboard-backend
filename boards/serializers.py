from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from boards.models import Board, Note


class BoardSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Note.objects.all())
    board = serializers.PrimaryKeyRelatedField(required=False, queryset=Board.objects.all())
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'notes', 'boards', 'board', 'owner']

    def validate(self, attrs):
        if 'board' in attrs and attrs['board'].owner != self.context['request'].user:
            raise PermissionDenied()

        return attrs


class NoteSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'content', 'board', 'owner']

    def validate(self, attrs):
        if 'board' in attrs and attrs['board'].owner != self.context['request'].user:
            raise PermissionDenied()

        return attrs
