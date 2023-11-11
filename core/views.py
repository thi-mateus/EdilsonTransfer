from django.shortcuts import render

from core.forms import BookingForm
from .models import Slider


def index(request):
    form = BookingForm()

    # Hero Slider
    hero_slider = Slider.objects.all()
    for slider in hero_slider:
        print(slider.imagem.url)

    context = {
        'form': form,
        'hero_slider': hero_slider
    }

    return render(request, 'index.html', context)
