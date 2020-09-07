from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here. - this will make it visibile on the admin page
# admin.site.register(Post)
from .models import SiteUser, UserRecipe, ExternalRecipe, Question, Choice


# admin.site.register(User)
admin.site.register(UserRecipe)
admin.site.register(ExternalRecipe)
admin.site.register(Question)
admin.site.register(Choice)