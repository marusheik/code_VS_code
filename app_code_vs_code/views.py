from django.shortcuts import render




# Create your views here.
def loadIndex(request):
    return render( request, "index.html")
