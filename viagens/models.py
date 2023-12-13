from django.db import models
from django.utils import timezone


class Viagem(models.Model):
    hora_solicitacao = models.DateTimeField(
        verbose_name="Hora da Solicitação")
    nome_usuario = models.CharField(
        max_length=100, verbose_name="Nome", blank=False)
    email_usuario = models.EmailField(
        verbose_name="Email", blank=True, null=True)
    telefone_usuario = models.CharField(
        max_length=20, verbose_name="Telefone", blank=False)
    origem = models.CharField(
        max_length=255, verbose_name="Origem", blank=False)
    destino = models.CharField(
        max_length=255, verbose_name="Destino", blank=False)
    passageiros = models.IntegerField(
        verbose_name="Quantidade de Passageiros", blank=True, null=True)
    data_ida = models.DateField(
        verbose_name="Data da Ida", blank=False)
    data_volta = models.DateField(
        verbose_name="Data da Volta", blank=True, null=True)
    hora_ida = models.TimeField(
        verbose_name="Hora da Ida", blank=False)
    hora_volta = models.TimeField(
        verbose_name="Hora da Volta", blank=True, null=True)
    ida_e_volta = models.CharField(max_length=20, choices=[(
        '1', 'Somente Ida'), ('2', 'Ida e Volta')], verbose_name="Ida e Volta?", blank=True, null=True)
    mensagem = models.TextField(
        verbose_name="Sua Mensagem", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.hora_solicitacao:
            self.hora_solicitacao = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome_usuario}: de {self.origem} para {self.destino} em {self.data_ida} às {self.hora_ida}'

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
