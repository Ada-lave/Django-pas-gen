from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    password= ''
    charsets = list('qwertyuiopasdfghjklzxcvbnm')
    lenght = int(request.GET.get('lenght',12))

    if request.GET.get('uppercase'):
        charsets.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    
    if request.GET.get('special'):
        charsets.extend(list('!@#$%^&*()_'))

    if request.GET.get('Number'):
        charsets.extend(list('1234567890'))

    for x in range(lenght):
        password+= random.choice(charsets)
    return render(request,'generator/pass.html', {'password':password})

def opis(request):
    return render(request,'generator/subs.html')
