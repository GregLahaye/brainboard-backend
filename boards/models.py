from django.db import models


class Board(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    board = models.ForeignKey('Board', null=True, blank=True, related_name='boards', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    board = models.ForeignKey('Board', related_name='notes', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
