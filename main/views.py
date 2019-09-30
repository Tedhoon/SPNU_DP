from django.shortcuts import render
from .models import MenuList

def index(request):
    return render(request , 'index.html')


def menu(request):
    menu = MenuList.objects.all()

    return render(request, 'menu.html', {'menu' : menu})


def bus(request):
    return render(request, 'bus.html')