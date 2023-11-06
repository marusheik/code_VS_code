from django.urls import path
from .views import VRegister, VLog_Out, VLogin
from django.urls import path, include
from app_code_vs_code.views import loadIndex
from allauth.account.views import LoginView, SignupView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignupView.as_view(), name='Register'),
    path('logout/', VLog_Out, name='logout'),
    path('', loadIndex, name='index'),
    # path('accounts/register/',VRegister.as_view(), name="Register"),
    # path('accounts/login/',VLogin, name="login"),
    # path('logout',VLog_Out, name="logout"),
    
]