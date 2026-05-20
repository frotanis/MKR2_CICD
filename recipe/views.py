from django.shortcuts import render
from .models import Recipe

def main(request):
    # recipes_2023 = Recipe.objects.filter(created_at__year=2023)

    context = {
        'recipes': []
    }
    return render(request, 'main.html', context)


def recipe_detail(request, recipe_id):
    # Шукаємо рецепт за його id. Якщо такого немає - видасть помилку 404
    recipe = get_object_or_404(Recipe, id=recipe_id)

    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)