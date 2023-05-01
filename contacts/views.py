from django.shortcuts import render
from .models import Contact, OpenHours


def contacts_view(request):
    """View returning the contacts page"""
    contacts = Contact.objects.first()
    open_hours = OpenHours.objects.all()

    context = {
        'contacts': contacts,
        'open_hours': open_hours,
    }

    return render(request, 'contacts/contacts.html', context)
