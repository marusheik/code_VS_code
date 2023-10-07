from django.urls import path
from . import views

urlpatterns = [
    path('',views.loadRegister, name="Register")
]