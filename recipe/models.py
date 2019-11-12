import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    """ """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, **options)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

class Recipe(models.Model):
    """ """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
