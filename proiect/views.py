from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'proiect/home.html', context)

def about(request):
    return render(request, 'proiect/about.html',{'title': 'About'})