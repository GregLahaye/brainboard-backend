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

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, args, kwargs)

        board_id = kwargs['pk']

        boards_queryset = Board.objects.filter(board=board_id)
        notes_queryset = Note.objects.filter(board=board_id)

        boards = BoardSerializer(boards_queryset, many=True).data
        notes = NoteSerializer(notes_queryset, many=True).data

        response.data['boards'] = boards
        response.data['notes'] = notes

        return response


class NoteViewSet(ModelWithOwnerViewSet):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
