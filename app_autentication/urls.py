from django.urls import path
from .views import VRegister, vLog_Out
from app_code_vs_code.views import loadIndex


urlpatterns = [
    path('register/',VRegister.as_view(), name="Register"),
    path('logout',vLog_Out, name="logout"),
    path('', loadIndex, name='index'),
]