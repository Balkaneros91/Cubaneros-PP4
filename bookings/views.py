from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reservation_booking.models import Booking


@login_required
def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'Bookings/booking_list.html', context)


def booking_edit(request):
    pass


def booking_delete(request):
    pass
