from django.db import models


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, default='')
    position = models.IntegerField()
    note = models.ForeignKey(
        'Note', null=True, blank=True, related_name='notes', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
