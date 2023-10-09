from django.urls import path
from .views import VRegister, VLog_Out, VLogin
from app_code_vs_code.views import loadIndex


urlpatterns = [
    path('register/',VRegister.as_view(), name="Register"),
    path('login/',VLogin, name="login"),
    path('logout',VLog_Out, name="logout"),
    path('', loadIndex, name='index'),
]