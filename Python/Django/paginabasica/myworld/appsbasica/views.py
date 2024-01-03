from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    return render(request, "appsbasica/home.html")

def tienda(request):
    return render(request, "appsbasica/tienda.html")

def blog(request):
    return render(request, "appsbasica/blog.html")

def contacto(request):
    return render(request, "appsbasica/contacto.html") 