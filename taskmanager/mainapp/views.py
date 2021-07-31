from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Customer
from datetime import date
from .forms import UpdateTaskForm


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

    a = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
        return redirect(taskmanager)
    else:
        form = UpdateTaskForm(initial={'note': task.note, 'status': task.status})

    context = {'task': task, 'customer': customer, 'form': form}
    return render(request, 'mainapp/update_task.html', context)


def connection(request):
    return render(request, 'mainapp/connection.html')


def index(request):
    return render(request, 'mainapp/index.html')
