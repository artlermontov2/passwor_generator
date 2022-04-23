from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return render(request, 'generator/index.html', {})


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()-_+=;:,./?\~'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 8))
    the_pass = ''

    for _ in range(length):
        the_pass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_pass})


def about(request):
    return render(request, 'generator/about.html')