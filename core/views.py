from django.shortcuts import render
from django.contrib import messages

from .models import Slider
from viagens.forms import ViagemForm


def home(request):
    print(request.user)
    # Hero Slider
    hero_slider = Slider.objects.all().order_by('ordem')

    # Booking area

    context = {
        'hero_slider': hero_slider,
    }

    return render(request, 'core/pages/home.html', context)
