from django.contrib import admin

from boards.models import Board, Note

admin.site.register(Board)
admin.site.register(Note)
