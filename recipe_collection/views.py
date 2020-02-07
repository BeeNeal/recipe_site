from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ExternalRecipe, UserRecipe, Ingredient

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the recipe collection site index.")

def ext_recipe_display(request, id):
    recipes = ExternalRecipe.objects.filter(id=id)
    title = recipes[0].title
    return HttpResponse("Hello world - you're looking at {}".format(title))