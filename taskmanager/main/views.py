from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.decorators import login_required

from .models import Task, Project

def index (request):
    tasks = Task.objects.order_by("-id")
    return render (request, "main/index.html", {"title":"Formula 1® Racing","tasks":tasks})

def about (request):
    return render (request, "main/about.html")

def race (request):
    return render (request, "main/race.html")

def const(request):
    return render (request, "main/const.html")

def test(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "main/test.html", context)

def test_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'main/test_detail.html', context)

def reverse (request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request,'main/reverse.html', {'usertext':user_text,'reversedtext':reversed_text})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            messages.success(request,"Вы успешно зарегистрированы!")
            return redirect ("login")
        else:
            messages.error(request,"Ошибка регистрации!")
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = UserLoginForm()
    return render(request, "main/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")





