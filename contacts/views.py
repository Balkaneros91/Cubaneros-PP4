from django.shortcuts import render


def contacts_view(request):
    """View returning the contacts page"""

    context = {}

    return render(request, 'contacts/contacts.html', context)
