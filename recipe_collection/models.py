import uuid  # creates unique ids
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(models.Model):
    """ """

    email = models.EmailField(max_length=254, )
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50) 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    zipcode = models.IntegerField()
    # image = models.ImageField()  # requires pillow library **to-do**

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.id}, username={self.user_name}, email={self.email}>"

    def __str__(self):
        return self.user_name



class UserRecipe(models.Model):
    """ """
    
    author_id = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = ArrayField(ArrayField(models.CharField(max_length=50, blank=True)))
    instructions = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    tags = ArrayField(ArrayField(models.CharField(max_length=50)))
    # image = models.ImageField(upload_to=None, 
    #                           height_field=None,
    #                           width_field=None, 
    #                           max_length=100, 
    #                          )   # **to-do**

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.title}>"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ExternalRecipe(models.Model):
    """Most recipes - users save recipe URL, perhaps add notes about it. """

    title = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    has_been_made = models.BooleanField()
    notes = models.TextField()
    tags = ArrayField(ArrayField(models.CharField(max_length=50)))

    def __str__(self):
        return self.title

class MeasurementUnits(models.Model):
    """ """

    measurement_description = models.TextField()


class MeasurementQuantity(models.Model):
    """ """

    quantity_amount = models.TextField()


class Ingredient(models.Model):
    """ """

    name = models.TextField()
    tags = ArrayField(ArrayField(models.CharField(max_length=50)))

    def __str__(self):
        return self.name
