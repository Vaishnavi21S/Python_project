# recipes/admin.py
from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'servings')

admin.site.register(Recipe, RecipeAdmin)

