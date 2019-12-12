import uuid  # creates unique ids
from django.conf import settings
from django.db import models
from django.utils import timezone

# to-do
# do I need to do the ids? Django has built in

class User(models.Model):
    """ """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, )
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)

class Recipe(models.Model):
    """ """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to=None, 
                              height_field=None,
                              width_field=None, 
                              max_length=100, 
                             )
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MeasurementUnits(models.Model):
    """ """

    measurement_description = models.TextField()


class MeasurementQuantity(models.Model):
    """ """

    quantity_amount = models.TextField()


class Ingredient(model.Models):
    """ """

    ingredient_name = models.TextField()
    tags = models.TextField()  # will use arrayField when port to postgres


class SavedRecipes(model.Models):
    """Join table for recipes that users want to try """

    user = (models.ForeignKey(User.id))
    saved_recipe = (models.ForeignKey(Recipe.id))
    saved_date = models.DateTimeField(default=timezone.now)