from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
