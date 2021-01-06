from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)
