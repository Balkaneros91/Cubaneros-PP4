from django.shortcuts import render


def home_view(request):
    """View returning the index page"""

    context = {}

    return render(request, 'restaurant/index.html', context)
