from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from boards.models import Note
from boards.serializers import NoteSerializer
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)

    def retrieve(self, request, *args, **kwargs):
        query = Note.objects.get(owner=self.request.user, note=None)

        user = UserSerializer(request.user).data
        note = NoteSerializer(query).data

        response = Response(user)

        response.data["note"] = note

        return response
