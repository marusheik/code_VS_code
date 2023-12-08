from django.shortcuts import render
from app_exercises.models import Exercise
from django.shortcuts import render, get_object_or_404

# Create your views here.
def loadConsole(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render( request, "console.html", {'exercise': exercise})


