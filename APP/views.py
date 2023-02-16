from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse()

def curo(request):
    return render(request,'APP'/inicio.html)

def alumno(request):
    return HttpResponse()

def profesor(request):
    return HttpResponse()


def camada(request):
    return HttpResponse()