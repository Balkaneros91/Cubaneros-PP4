from django.shortcuts import render


def about_view(request):
    """View returning the about page"""

    context = {}

    return render(request, 'about/about.html', context)
