import random
from django.core.cache import cache
from django.shortcuts import render
from app_exercises.models import Exercise, Solution



# Create your views here.
def loadIndex(request):
    return render( request, "index.html")

def loadDashboard(request):
    
    cache_key = 'random_exercises'
    random_exercises = cache.get(cache_key)
    
    if random_exercises is None:
        
        exercises = Exercise.objects.all()
        random_exercises = random.sample(list(exercises), 2)
        cache.set(cache_key, random_exercises, 86400)
    
    user = request.user
    solved_exercises_count = Solution.objects.filter(user=user).count()
    return render( request, "dashboard.html", {'exercises': random_exercises, 'solved_exercises_count': solved_exercises_count})
