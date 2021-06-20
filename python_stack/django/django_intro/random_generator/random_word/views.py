from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    return render(request, 'index.html')