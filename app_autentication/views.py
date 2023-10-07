from django.shortcuts import render

# Create your views here.
def loadRegister(request):
    return render(request,'register/register.html')
