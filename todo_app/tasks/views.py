from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def remaining(request):
    return render(request, 'remaining.html')

def completed(request):
    return render(request, 'completed.html')

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