from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from boards.models import Note


class NoteSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        many=True, required=False, queryset=Note.objects.all())
    note = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Note.objects.all())
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'content', 'notes', 'note', 'owner']

    def validate(self, attrs):
        if 'board' in attrs and attrs['board'].owner != self.context['request'].user:
            raise PermissionDenied()

        return attrs
