from django.shortcuts import render, redirect
from django.http import HttpResponse
from retrospection.models import Thought, Time
from retrospection.form import ThoughtForm
from retrospection.form import TimeForm
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required
def retro(request):
    return render(request, 'retro.html')


@login_required
def look(request):

    if request.method == "POST":
        #data = Thought.objects.filter(manager = request.user)
        form = TimeForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            #print(time)
            today = timezone.now().date()
            if time == "yesterday":
                #print("yesterday selected")
                yesterday = timezone.now().date() - timedelta(days=1)
                data = Thought.objects.filter(date__gte=yesterday,  manager = request.user)
            elif time == "lastweek":
                #print("last week selected")
                week = timezone.now().date() - timedelta(days=7)
                data = Thought.objects.filter(date__gte=week, manager = request.user)
            elif time == "lastmonth":
                #print("last month selected")
                month = timezone.now().date() - timedelta(days=30)
                data = Thought.objects.filter(date__gte=month,  manager = request.user )
            elif time == "lastyear":
                year = timezone.now().date() - timedelta(days=365)
                data = Thought.objects.filter(date__gte=year, manager = request.user)
            elif time == "forever":
                data = Thought.objects.filter(manager = request.user) 
            elif time == "today":
                data = Thought.objects.filter(date__gte=today, manager = request.user)

            #implementation of Pagination
           #paginator = Paginator(data, 7)
           # page = request.GET.get('pg')
            #refreshing data
            #data = paginator.get_page(page)
            return render(request,'look.html', {'data' : data})
    return render(request, 'look.html')


def submit(request):
    return render(request, 'submit.html')

def index(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                instance.manager = request.user
                instance.save()
            except:
                return redirect('login')

        return redirect('submit')

    else:
        return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'sign.html')