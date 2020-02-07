from django.contrib import admin

# Register your models here. - this will make it visibile on the admin page
# admin.site.register(Post)
from .models import User, UserRecipe, ExternalRecipe
admin.site.register(User)
admin.site.register(UserRecipe)
admin.site.register(ExternalRecipe)