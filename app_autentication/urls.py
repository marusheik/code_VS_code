from django.urls import path
from .views import VRegister

urlpatterns = [
    path('',VRegister.as_view(), name="Register")
]