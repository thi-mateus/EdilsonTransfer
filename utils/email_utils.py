# utils/email_utils.py
import os
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

from utils.datetime_utils import format_date, format_time


def enviar_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)


def email_agendamento(form):
    subject = "Agendamento de Viagem | Edilson Transfer"
    from_email = 'edilsontransfernatal@gmail.com'
    print(from_email)
    message = msg_agendamento(form)

    to = [form.cleaned_data.get("email_usuario"),]

    mail = EmailMessage(
        subject=subject,
        body=message['mensagem_cliente'],
        from_email=from_email,
        to=to,
        headers={'Reply-To': from_email}
    )
    mail.send()

    to = [from_email,]
    mail = EmailMessage(
        subject=subject,
        body=message['mensagem_motorista'],
        from_email=from_email,
        to=to,
        headers={'Reply-To': from_email}
    )
    mail.send()


def msg_agendamento(form):
    nome_usuario = form.cleaned_data.get("nome_usuario")
    email_usuario = form.cleaned_data.get("email_usuario")
    telefone_usuario = form.cleaned_data.get("telefone_usuario")

    origem = form.cleaned_data.get("origem")
    destino = form.cleaned_data.get("destino")

    data_ida = form.cleaned_data.get("data_ida")
    hora_ida = form.cleaned_data.get("hora_ida")
    data_volta = form.cleaned_data.get("data_volta")
    hora_volta = form.cleaned_data.get("hora_volta")

    ida_e_volta = form.cleaned_data.get("ida_e_volta")

    passageiros = form.cleaned_data.get("passageiros")

    mensagem = form.cleaned_data.get("mensagem")

    saudacao_cliente = ""
    if nome_usuario:
        saudacao_cliente += f'Prezado(a) {nome_usuario}, '
    else:
        nome_usuario = 'Cliente, '
    saudacao_cliente += 'recebemos o seu agendamento de viagem.\n'

    saudacao_motorista = ""
    saudacao_motorista += f'Prezado(a) (Motorista), '
    saudacao_motorista += 'você recebeu uma solicitação de agendamento de viagem.\n'

    dados_cliente = ""
    dados_cliente += f'DADOS DO CLIENTE\n'

    if nome_usuario:
        dados_cliente += f'Nome: {nome_usuario}\n'

    if email_usuario:
        dados_cliente += f'Email: {email_usuario}\n'

    if telefone_usuario:
        dados_cliente += f'Telefone: {telefone_usuario}\n'

    dados_viagem = ""
    dados_viagem += f'DADOS DA VIAGEM\n'

    if origem:
        dados_viagem += f'Origem: {origem}\n'

    if destino:
        dados_viagem += f'Destino: {destino}\n'

    if data_ida:
        dados_viagem += f'Data da Ida: {format_date(data_ida)}\n'

    if hora_ida:
        dados_viagem += f'Hora da Ida: {format_time(hora_ida)}\n'

    if data_volta:
        dados_viagem += f'Data da Volta: {format_date(data_volta)}\n'

    if hora_volta:
        dados_viagem += f'Hora da Volta: {format_time(hora_volta)}\n'

    if ida_e_volta:
        if ida_e_volta == '1':
            dados_viagem += f'Ida e Volta: não \n'
        elif ida_e_volta == '2':
            dados_viagem += f'Ida e Volta: sim \n'

    if passageiros:
        dados_viagem += f'Passageiros: {passageiros}\n'

    mensagem_ao_motorista = ""

    if mensagem:
        mensagem_ao_motorista = f'MENSAGEM AO MOTORISTA\n'
        mensagem_ao_motorista += f'Mensagem: {mensagem}'

    mensagem_cliente = f'{saudacao_cliente}\n{dados_cliente}\n{dados_viagem}\n{mensagem_ao_motorista}'
    mensagem_motorista = f'{saudacao_motorista}\n{dados_cliente}\n{dados_viagem}\n{mensagem_ao_motorista}'

    mensagem_agendamento = {
        'mensagem_cliente': mensagem_cliente,
        'mensagem_motorista': mensagem_motorista,
    }

    return mensagem_agendamento
