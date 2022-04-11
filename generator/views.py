from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):

    return render(request, 'generator/home.html')

def about(request):

    return render(request, 'generator/about.html')

def password(request):

    chars = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length', 12))  # 12 это значение по умолчанию если дина не задана явно
    if request.GET.get('uppercase'):
        chars.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*'))

    thepassword = ''

    for _ in range(length):
        thepassword += random.choice(chars)

    return render(request, 'generator/password.html', {'password': thepassword})
