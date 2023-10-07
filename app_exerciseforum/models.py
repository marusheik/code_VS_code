from django.db import models

class Comment(models.Model):
    fecha = models.DateField()
    content = models.TextField()
