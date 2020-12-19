from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    return render(request, 'login.html')

def sign(request):
    register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form' : register_form})