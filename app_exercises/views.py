from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, Solution
from django.urls import reverse


def exercise_list(request):
    language_filter = request.GET.get('language', None)
    exercises = Exercise.objects.all()

    # Filtrar por lenguaje si se selecciona
    if language_filter:
        exercises = exercises.filter(language=language_filter)

    return render(request, 'exercise_list.html', {'exercises': exercises, 'language_filter': language_filter})

@login_required
def save_solution(request, exercise_id):
     if request.method == 'POST':

        code = request.POST.get('code')
        print(f'Tipo de code: {type(code)}')
        print(f'Contenido de code: {code}')
        exercise = Exercise.objects.get(pk=exercise_id)
        user = request.user

        Solution.objects.create(
            exercise=exercise,
            user=user,
            code=code,
        )

        # Redirigir a la vista de soluciones después de guardar
        # return redirect('show_solutions')
        return redirect(reverse('show_solutions') + f'?exercise_id={exercise_id}')

    
    # return redirect('alguna_otra_vista')
def show_solutions(request):
    exercise_id = request.GET.get('exercise_id')

    if exercise_id:
        solutions = Solution.objects.filter(exercise__id=exercise_id)
    else:
        solutions = Solution.objects.all()

    return render(request, 'show_solutions.html', {'solutions': solutions})
    # solutions = Solution.objects.all()
    # return render(request, 'show_solutions.html', {'solutions': solutions})   
