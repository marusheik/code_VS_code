# pylint: disable=E1101
from django.db import models

class Exercise(models.Model):

    statement = models.TextField()
    language = models.CharField(max_length=20, choices=[
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
    ])
    def __str__(self):
        return f"{self.statement} - {self.get_language_display()}"
