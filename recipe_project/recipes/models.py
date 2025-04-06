# # recipes/models.py

from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()
    servings = models.PositiveIntegerField(default=1)
    ingredients = models.JSONField(default=list)

    def __str__(self):
        return self.name

    def adjust_ingredients_for_servings(self, servings):
        adjusted_ingredients = []
        for ingredient in self.ingredients:
            adjusted_ingredient = ingredient.copy()
            try:
                adjusted_ingredient['quantity'] = float(ingredient['quantity']) * (servings / self.servings)
            except (ValueError, TypeError):
                adjusted_ingredient['quantity'] = 0
            adjusted_ingredients.append(adjusted_ingredient)
        return adjusted_ingredients
