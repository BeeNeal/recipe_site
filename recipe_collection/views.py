from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User, ExternalRecipe, UserRecipe, Ingredient

# Create your views here.


def index(request):

    current_user = User.objects.filter(id=1)
    print(current_user)
    featured_recipe = ExternalRecipe.objects.filter(id=1)
    context = {
        'current_user': current_user[0].first_name,
        'featured_recipe': featured_recipe
    }
    print(context)
    return render(request, "recipe_collection/index.html", context)

def ext_recipe_display(request, id):
    recipes = ExternalRecipe.objects.filter(id=id)
    title = recipes[0].title
    return HttpResponse("Hello world - you're looking at {}".format(title))


def saved_recipe(request, user_id):
    recipes = ExternalRecipe.objects.filter(user_id=user_id, has_been_made=True)
