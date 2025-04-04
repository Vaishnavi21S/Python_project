from django.shortcuts import render, get_object_or_404
from .models import Recipe

def main_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/main.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    servings = float(request.GET.get('servings', recipe.servings))

    adjusted_ingredients = recipe.adjust_ingredients_for_servings(servings)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': adjusted_ingredients,
        'servings': servings,
    })
