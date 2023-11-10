from django.shortcuts import render

from core.forms import BookingForm


def index(request):
    form = BookingForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
