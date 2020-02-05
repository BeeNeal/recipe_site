from django.urls import path

from . import views

# path(route, view, kwargs(dict), name)
urlpatterns = [
    path('', views.index, name='index'),
    path("", views.recipe_display, name='recipe_display'),
]