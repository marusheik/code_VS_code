# pylint: disable=E1101
from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):

    statement = models.TextField()
    language = models.CharField(max_length=20, choices=[
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
    ])
    def __str__(self):
        return f"{self.statement} - {self.get_language_display()}"
    
class Solution(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solución para {self.exercise} por {self.user.username}"
