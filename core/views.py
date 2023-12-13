from django.shortcuts import render

from .models import Slider


def home(request):

    # Hero Slider
    hero_slider = Slider.objects.all().order_by('ordem')

    # Booking area

    context = {
        'hero_slider': hero_slider,
    }

    return render(request, 'core/pages/home.html', context)
