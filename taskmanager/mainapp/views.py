from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tasks
from datetime import date


def index(request):
    tasks = Tasks.objects.all()
    tasks_not_started = Tasks.objects.filter(status=1)
    tasks_started = Tasks.objects.filter(status=2)
    tasks_finished = Tasks.objects.filter(status=3)
    today = date.today()
    context = {
        'tasks': tasks,
        'tasks_not_started': tasks_not_started,
        'tasks_started': tasks_started,
        'tasks_finished': tasks_finished,
        'today': today
    }
    return render(request, 'mainapp/index.html', context)


def update_task(request, pk):
    task = Tasks.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'mainapp/update_task.html', context)


def connection(request):
    return render(request, 'mainapp/connection.html')


def hello():
    print("HELLO")
