from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from viagens.forms import ViagemForm
from utils.email_utils import email_agendamento


def agendar_viagem(request):
    if str(request.method) == 'POST':
        form = ViagemForm(request.POST)

        if form.is_valid():

            form.save()

            # Enviar e-mail de notificação
            email_agendamento(form)

            messages.success(
                request, 'Viagem agendada com sucesso. Entraremos em contato.')

            # Limpa o formulário após sucesso no agendamento
            form = ViagemForm()

            return redirect(reverse('home') + '#booking-area')

        else:

            messages.error(request, 'Erro ao agendar a viagem.')

    else:
        form = ViagemForm()

    context = {
        'form': form
    }

    return render(request, 'viagens/pages/book-ride.html', context)
