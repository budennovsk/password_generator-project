import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):


    characters = list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get('uppercase'):
        characters.extend(list('QWRTYUIOOLKJHNBGVCCVBNMZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    lenght = int(request.GET.get('lenght'))
    thepassword = ""
    for i in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})


def about_me(request):
    return render(request, 'generator/about_me.html')