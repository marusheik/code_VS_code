from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, Solution


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
        return redirect('show_solutions')

    # Si no es una solicitud POST, redirigir o renderizar según tus necesidades
    # return redirect('alguna_otra_vista')
def show_solutions(request):
    solutions = Solution.objects.all()
    return render(request, 'show_solutions.html', {'solutions': solutions})   
