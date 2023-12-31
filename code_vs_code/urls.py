"""
URL configuration for code_vs_code project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_code_vs_code.views import loadIndex, loadDashboard
from app_console.views import loadConsole
from app_exercises.views import exercise_list, save_solution, show_solutions
# from app_autentication.views import loadRegister


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', loadIndex, name='index'),
    path('', include('app_autentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('console/<int:exercise_id>', loadConsole, name='console'),
    path('exercises/', exercise_list, name='exercises'),
    path('save_solution/<int:exercise_id>/', save_solution, name='save_solution'),
    path('show_solutions/', show_solutions, name='show_solutions'),
    path('dashboard/', loadDashboard, name='dashboard'),
    path('show_solutions<int:exercise_id>/', show_solutions, name='show_solutions'),
]
