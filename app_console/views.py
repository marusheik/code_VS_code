from django.shortcuts import render

# Create your views here.
def loadConsole(request):
    return render( request, "console.html")


