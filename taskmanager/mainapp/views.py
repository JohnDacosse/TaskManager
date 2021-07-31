from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Customer
from datetime import date


@login_required
def taskmanager(request):
    tasks = Task.objects.all()
    tasks_not_started = Task.objects.filter(status=1)
    tasks_started = Task.objects.filter(status=2)
    tasks_finished = Task.objects.filter(status=3)
    today = date.today()
    context = {
        'tasks': tasks,
        'tasks_not_started': tasks_not_started,
        'tasks_started': tasks_started,
        'tasks_finished': tasks_finished,
        'today': today
    }
    return render(request, 'mainapp/taskmanager.html', context)


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    customer = get_object_or_404(Customer, pk=task.customer_id)
    context = {'task': task, 'customer': customer}
    return render(request, 'mainapp/update_task.html', context)


def connection(request):
    return render(request, 'mainapp/connection.html')


def index(request):
    return render(request, 'mainapp/index.html')
