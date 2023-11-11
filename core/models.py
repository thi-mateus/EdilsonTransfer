from django.db import models


class Slider(models.Model):
    ordem = models.IntegerField()
    saudacao = models.CharField(
        max_length=50, default="Bem Vindo à Edilson Transfer!")
    titulo = models.CharField(max_length=50, )
    texto = models.TextField()
    botao_agendar = models.TextField(
        default="Desejo fazer uma cotação com a Edilson Transfer.")
    # Tamanho da imagem: 1920 x 1280
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.ordem}: {self.titulo}'
