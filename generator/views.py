import random
from django.shortcuts import render



# Create your views here.
def home(request: object) -> object:
    """ Отображение страницы HOME """
    return render(request, 'generator/home.html')


def password(request: object) -> object:
    """ Генерация пароля с последующим отображением на страницы GENERATE"""
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
    return render(request, 'generator/password.html', {'password': thepassword})


def about_me(request: object) -> object:
    """Отображение страницы ABOUT"""
    return render(request, 'generator/about_me.html')
