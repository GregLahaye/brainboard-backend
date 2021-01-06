from rest_framework import viewsets

from boards.models import Board, Note
from boards.serializers import BoardSerializer, NoteSerializer


class ModelWithOwnerViewSet(viewsets.ModelViewSet):
    model = None

    def get_queryset(self):
        assert self.model is not None
        user = self.request.user
        return self.model.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardViewSet(ModelWithOwnerViewSet):
    model = Board
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class NoteViewSet(ModelWithOwnerViewSet):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
