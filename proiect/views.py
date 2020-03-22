from django.shortcuts import render

def home(request):
    return render(request, 'proiect/home.html')

def about(request):
    return render(request, 'proiect/about.html')