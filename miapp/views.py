from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"mensaje": "Bienvenido a mi proyecto Django", "alumna": "Milena Fernández"}
    return render(request,"miapp/index.html", context)