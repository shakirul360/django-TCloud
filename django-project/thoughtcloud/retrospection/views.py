from django.shortcuts import render, redirect
from django.http import HttpResponse
from retrospection.models import Thought
from retrospection.form import ThoughtForm
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def retro(request):
    if request.method == "POST":
        data = Thought.objects.all
        form = ThoughtForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            today = timezone.now().date()
            if time == "Yesterday":
                yesterday = timezone.now().date() - timedelta(days=1)
                data = Thought.objects.filter(date__gte=yesterday, date__lt=today)
            elif time == "lastweek":
                week = timezone.now().date() - timedelta(days=7)
                data = Thought.objects.filter(date__gte=week, date__lt=today)
            elif time == "Last Month":
                month = timezone.now().date() - timedelta(days=30)
                data = Thought.objects.filter(date__gte=month, date__lt=today)
            elif time == "Last Year":
                year = timezone.now().date() - timedelta(days=365)
                data = Thought.objects.filter(date__gte=year, date__lt=today)
            elif time == "Forever":
                data = Thought.objects.all 
            else:
                data = Thought.objects.filter(date__gte=today, date__lt=today)

            return render(request,'look.html', {'data' : data})
        #  Do something when form is invalid.
        #      Maybe just removing the else below this, so you'll get retro.html
        else:
            print(form.is_valid())
            print(form.errors)
            #paginator = Paginator(data, 5)
            #page = request.GET.get('pg')
            #data = paginator.get_page(page)
            return render(request, 'look.html', {'data': data})
    return render(request, 'retro.html')



def look(request):
    all_thoughts = Thought.objects.all
    today = timezone.now().date()
    week = timezone.now().date() - timedelta(days=8)
    month = timezone.now().date() - timedelta(days=31)
    year = timezone.now().date() - timedelta(days=365)
    yesterday = timezone.now().date() - timedelta(days=1)
    #monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    #monday_of_this_week = monday_of_last_week + timedelta(days=7)
    data = Thought.objects.filter(date__gte=month, date__lt=today)
    #return HttpResponse("welcome from django")
    
    return render(request, 'look.html', {'data' : data})


def submit(request):
    #return HttpResponse("welcome from django")
    context = {
        'welcome_text' : "welcome from submit",
    }
    return render(request, 'submit.html')

def index(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            print(form.is_valid())
        return redirect('submit')
    else:
        return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'sign.html')