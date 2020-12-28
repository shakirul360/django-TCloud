from django.shortcuts import render, redirect
from django.http import HttpResponse
from retrospection.models import Thought, Time
from retrospection.form import ThoughtForm, TimeForm
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def retro(request):
    return render(request, 'retro.html')


@login_required
def look(request):

    if request.method == "POST":
        #data = Thought.objects.filter(manager = request.user)
        form = TimeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            time = form.cleaned_data['time']
            #print(time)
            today = timezone.now().date()
            if time == "yesterday":
                #print("yesterday selected")
                yesterday = timezone.now().date() - timedelta(days=1)
                data = Thought.objects.filter(date__gte=yesterday)
            elif time == "lastweek":
                #print("last week selected")
                week = timezone.now().date() - timedelta(days=7)
                data = Thought.objects.filter(date__gte=week, date__lt=today)
            elif time == "lastmonth":
                #print("last month selected")
                month = timezone.now().date() - timedelta(days=30)
                data = Thought.objects.filter(date__gte=month, date__lt=today)
            elif time == "lastyear":
                year = timezone.now().date() - timedelta(days=365)
                data = Thought.objects.filter(date__gte=year, date__lt=today)
            elif time == "forever":
                data = Thought.objects.all 
            elif time == "today":
                data = Thought.objects.filter(date__gte=today)

            return render(request,'look.html', {'data' : data})
    print(request.method)
    print(form.is_valid())
    print(form.errors)
    return render(request, 'look.html')


def submit(request):
    context = {
        'welcome_text' : "welcome from submit",
    }
    return render(request, 'submit.html')

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

def test(request):
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'sign.html')