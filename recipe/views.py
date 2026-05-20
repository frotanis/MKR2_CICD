from django.shortcuts import render
# from .models import Recipe

def main(request):
    # recipes_2023 = Recipe.objects.filter(created_at__year=2023)

    context = {
        'recipes': []
    }
    return render(request, 'main.html', context)