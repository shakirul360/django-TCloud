from django.shortcuts import render, redirect 
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.

def sign(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account created"))
            return redirect('login')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form' : register_form})



def index(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
        #else:
        #    print(form.is_valid())
        #   print(form.errors)
        return redirect('submit')

    else:
        return render(request, 'index.html')