from django.shortcuts import render
from .models import Post


def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'proiect/home.html', context)

def about(request):
    return render(request, 'proiect/about.html',{'title': 'About'})