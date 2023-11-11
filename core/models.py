from PIL import Image

from django.db import models


class Slider(models.Model):
    ordem = models.PositiveSmallIntegerField()
    saudacao = models.CharField(
        max_length=50, default="Bem Vindo à Edilson Transfer!", verbose_name="saudação")
    titulo = models.CharField(max_length=50, verbose_name="título")
    texto = models.TextField()
    botao_agendar = models.TextField(
        default="Desejo fazer uma cotação com a Edilson Transfer.", verbose_name="Botão Agendar")
    # Tamanho da imagem: 1920 x 1280
    imagem = models.ImageField(
        upload_to='index/hero-slider/', verbose_name="Imagem (1920x1280)")

    def __str__(self):
        return f'{self.ordem}: {self.titulo}'

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)

            # Abre a imagem recém-carregada
            imagem = Image.open(self.imagem.path)

            # Define o tamanho desejado
            tamanho_desejado = (1920, 1280)  # Tamanho desejado

            # Calcula o fator de escala para manter a proporção original
            escala = max(tamanho_desejado[0] / float(imagem.width),
                         tamanho_desejado[1] / float(imagem.height))

            # Redimensiona mantendo a proporção
            nova_largura = int(imagem.width * escala)
            nova_altura = int(imagem.height * escala)
            imagem = imagem.resize((nova_largura, nova_altura), Image.LANCZOS)

            # Calcula as coordenadas para o recorte centrado
            left = (imagem.width - tamanho_desejado[0]) / 2
            top = (imagem.height - tamanho_desejado[1]) / 2
            right = (imagem.width + tamanho_desejado[0]) / 2
            bottom = (imagem.height + tamanho_desejado[1]) / 2

            # Corta a imagem para se ajustar ao tamanho desejado
            imagem = imagem.crop((left, top, right, bottom))

            # Salva a imagem redimensionada e cortada de volta no caminho original
            imagem.save(self.imagem.path)

        except (IOError, OSError, ValueError, Image.DecompressionBombError) as e:
            # Lida com exceções específicas do Pillow
            print(f"Erro ao processar a imagem: {e}")

        except (FileNotFoundError, PermissionError) as e:
            # Lida com exceções relacionadas a caminhos ou arquivos
            print(f"Erro de arquivo ao processar a imagem: {e}")

        except Exception as e:
            # Lida com exceções genéricas
            print(f"Erro inesperado ao processar a imagem: {e}")
