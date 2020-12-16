from django.shortcuts import render, redirect
from django.http import HttpResponse
from retrospection.models import Thought
from retrospection.form import ThoughtForm

# Create your views here.

def retro(request):
    #return HttpResponse("welcome from django")
    context = {
        'welcome_text' : "welcome from retro",
    }
    return render(request, 'retro.html')


def look(request):
    all_thoughts = Thought.objects.all

    #return HttpResponse("welcome from django")
    context = {
        'welcome_text' : "welcome from look",
    }
    return render(request, 'look.html', {'all_thoughts' : all_thoughts})


def submit(request):
    #return HttpResponse("welcome from django")
    context = {
        'welcome_text' : "welcome from submit",
    }
    return render(request, 'submit.html')

def tcloud(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('submit')
    else:
        return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')