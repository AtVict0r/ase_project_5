from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
    })

def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False)

    return render(request, 'remaining.html', {
        'todo': remaining_tasks,
    })

def completed(request):
    completed_tasks = Task.objects.filter(completed=True)

    return render(request, 'completed.html', {
        'completed': completed_tasks,
    })

def add(request):
    return render(request, 'add.html')

def delete(request):
    return render(request, 'delete.html')

def edit(request):
    return render(request, 'edit.html')

def search(request):
    return render(request, 'search.html')

def sort(request):
    return render(request, 'sort.html')

def detail(request):
    return render(request, 'detail.html')