from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.urls import reverse 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def VLogin(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,"usuario no valido")
        else:
            messages.error(request,"info incorrecta")
            
    form = AuthenticationForm()
    return render( request, "login/login.html", {"form":form})
   
def VLog_Out(request):
        logout(request)
        return redirect('index')
    
class VRegister(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render( request, "register/register.html", {"form":form} )
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            usuario = form.save()
        
            login(request, usuario)
        
            return redirect(reverse('index'))
        
        else:
            pass
            # for msg in form.error_messages:
            #     messages.error(request, form.error_messages[msg])
                
            # return render( request, "register/register.html", {"form":form} )
 


# Create your views here.
# def loadRegister(request):
#     return render(request,'register/register.html')
