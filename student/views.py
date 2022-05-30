from pydoc import describe
from turtle import title
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from courses.models import Mentee, Mentor, Group, Course
from open_lessons.models import Open_lessons
from blog.models import Post

from . forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from datetime import datetime
import requests

# Create your views here.

@login_required(login_url='login')
def dashboard_page(request):
    now = datetime.now()
    users = User.objects.all().filter().count()
    mentees = Mentee.objects.all().filter().count()
    mentors = Mentor.objects.all().filter().count()
    courses = Course.objects.all().filter().count()
    groups = Group.objects.all().filter().count()
    group = Group.objects.all()
    course = Course.objects.all()
    all_c = Post.objects.all().order_by('-date')
    page = Paginator(all_c, 4)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    appid = '88f4fd23a4a19c261b6e5e4fc98618ff'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    city = 'Tashkent'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=url, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = int(round(res['main']['temp'], 0))
    
    context ={
        'now':now,
        'mentees':mentees,
        'mentors':mentors,
        'courses':courses,
        'course':course,
        'groups':groups,
        'group':group,
        'all_c':all_c,
        'page':page,
        'description' : description,
        'icon':icon,
        'temp':temp,
        'city':city,
        'users':users,
    }
    return render(request, 'student/dashboard.html', context)

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            return redirect('login')
        else:
            form = CreateUserForm()

    context={

        'form' : form
    }
    return render(request, 'student/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username , password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('error_page')
    context={}

    return render(request, 'student/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def error_page(request):
    return render(request, 'student/error-404.html')

def profile(request):
    return render(request, 'student/user_profile.html')


