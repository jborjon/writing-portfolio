from django.db import models

class Piece(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    topic = models.CharField(max_length=50)
    image = models.FilePathField(path='/img')
