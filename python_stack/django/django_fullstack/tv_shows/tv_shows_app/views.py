from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard.html')

def new(request):
    return render(request, 'dashboard.html')

def create(request):
    return render(request, 'dashboard.html')

def view(request):
    return render(request, 'dashboard.html')

def edit(request):
    return render(request, 'dashboard.html')

def update(request):
    return render(request, 'dashboard.html')

def destroy(request):
    return render(request, 'dashboard.html')
