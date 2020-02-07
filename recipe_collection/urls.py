from django.urls import path

from . import views

# path(route, view, kwargs(dict), name)
urlpatterns = [
    path("", views.index, name='index'),
    # keep in mind "/"s!
    path("<int:id>/", views.ext_recipe_display, name='ext_recipe_display'),
]