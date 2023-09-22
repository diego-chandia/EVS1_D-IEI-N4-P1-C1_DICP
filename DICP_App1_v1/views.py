from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def view1(request):
    now = HttpResponse("<h1>Ola k ase</h1>")
    return now
def view2(request):
    now2 = HttpResponse("<h1>Hola, buenos dias</h1>")
    return now2