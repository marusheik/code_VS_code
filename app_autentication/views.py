from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib import messages

from django.urls import reverse 

from django.contrib.auth.forms import UserCreationForm


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
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render( request, "register/register.html", {"form":form} )
        

# Create your views here.
# def loadRegister(request):
#     return render(request,'register/register.html')
