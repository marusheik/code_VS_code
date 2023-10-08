from django.urls import path
from .views import VRegister
from app_code_vs_code.views import loadIndex


urlpatterns = [
    path('register/',VRegister.as_view(), name="Register"),
    path('', loadIndex, name='index'),
]