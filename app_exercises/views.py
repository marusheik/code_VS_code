from django.shortcuts import render
from .models import Exercise

def exercise_list(request):
    language_filter = request.GET.get('language', None)
    exercises = Exercise.objects.all()

    # Filtrar por lenguaje si se selecciona
    if language_filter:
        exercises = exercises.filter(language=language_filter)

    return render(request, 'exercise_list.html', {'exercises': exercises, 'language_filter': language_filter})
