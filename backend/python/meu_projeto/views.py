from django.shortcuts import render
from django.http import HttpResponse


def minha_view(request):
    return HttpResponse("Esta é a minha_view!")
