from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.succes(request, f'Account created for {username}!')
            return redirect('proiect-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
