from django.db import models

class Comment(models.Model):
    fecha = models.DateField()
    content = models.TextField()
    
class ProgLanguage(models.Model):
    name = models.CharField(max_length=30)