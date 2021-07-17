from django.shortcuts import render, get_object_or_404
from .models import Tasks, Clients
from datetime import date


def taskmanager(request):
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
    return render(request, 'mainapp/taskmanager.html', context)


def update_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    client = get_object_or_404(Clients, pk=task.client_id)
    context = {'task': task, 'client': client}
    return render(request, 'mainapp/update_task.html', context)


def connection(request):
    return render(request, 'mainapp/connection.html')


def hello():
    print("HELLO")
