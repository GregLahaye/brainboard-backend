from rest_framework import viewsets

from boards.models import Note
from boards.serializers import NoteSerializer


class ModelWithOwnerViewSet(viewsets.ModelViewSet):
    model = None

    def get_queryset(self):
        assert self.model is not None
        user = self.request.user
        return self.model.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteViewSet(ModelWithOwnerViewSet):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, args, kwargs)

        query = Note.objects.filter(owner=self.request.user, note=kwargs['pk'])

        notes = NoteSerializer(query, many=True).data

        response.data["notes"] = notes

        return response
