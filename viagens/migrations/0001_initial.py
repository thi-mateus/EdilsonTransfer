# Generated by Django 4.2.7 on 2023-12-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100, verbose_name='Nome')),
                ('email_usuario', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('telefone_usuario', models.CharField(max_length=20, verbose_name='Telefone')),
                ('origem', models.CharField(max_length=255, verbose_name='Origem')),
                ('destino', models.CharField(max_length=255, verbose_name='Destino')),
                ('passageiros', models.IntegerField(blank=True, null=True, verbose_name='Quantidade de Passageiros')),
                ('data_ida', models.DateField(verbose_name='Data da Ida')),
                ('data_volta', models.DateField(blank=True, verbose_name='Data da Volta')),
                ('hora_ida', models.TimeField(verbose_name='Hora da Ida')),
                ('hora_volta', models.TimeField(blank=True, verbose_name='Hora da Volta')),
                ('ida_e_volta', models.CharField(blank=True, choices=[('1', 'Somente Ida'), ('2', 'Ida e Volta')], max_length=20, verbose_name='Ida e Volta?')),
                ('mensagem', models.TextField(blank=True, verbose_name='Sua Mensagem')),
            ],
        ),
    ]
