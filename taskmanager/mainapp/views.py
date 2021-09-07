from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Customer
from datetime import date
from .forms import UpdateTaskForm


# Page principale de l'application
@login_required
def taskmanager(request):
    current_user_id = request.user
    tasks = Task.objects.all()
    tasks_not_started = Task.objects.filter(status=1, user=current_user_id)
    tasks_started = Task.objects.filter(status=2, user=current_user_id)
    tasks_finished = Task.objects.filter(status=3, user=current_user_id)
    today = date.today()
    context = {
        'tasks': tasks,
        'tasks_not_started': tasks_not_started,
        'tasks_started': tasks_started,
        'tasks_finished': tasks_finished,
        'today': today
    }
    return render(request, 'mainapp/taskmanager.html', context)


# Page de modification d'une tâche
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


# Page d'index
def index(request):
    return render(request, 'mainapp/index.html')


# Page de déconnexion
def logged_out(request):
    return render(request, 'mainapp/logout.html')


# Page de recherche d'un ou plusieurs clients
@login_required
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        current_user_id = request.user
        customers = Customer.objects.filter(name__icontains=searched)
        print(customers)
        tasks_searched = []
        for customer in customers:
            tasks_searched.append(Task.objects.filter(customer_id=customer.id, user=current_user_id))
        return render(request, 'mainapp/search.html', {'tasks_searched': tasks_searched})
    else:
        return render(request, 'mainapp/search.html', {})
