from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the recipe collection site index.")

def recipe_display(request):
    return HttpResponse("Hello world - you're at recipe display")