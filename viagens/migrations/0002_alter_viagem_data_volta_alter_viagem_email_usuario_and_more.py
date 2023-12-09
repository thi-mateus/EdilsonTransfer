# Generated by Django 4.2.7 on 2023-12-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='data_volta',
            field=models.DateField(blank=True, null=True, verbose_name='Data da Volta'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='email_usuario',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='hora_volta',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora da Volta'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='ida_e_volta',
            field=models.CharField(blank=True, choices=[('1', 'Somente Ida'), ('2', 'Ida e Volta')], max_length=20, null=True, verbose_name='Ida e Volta?'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='mensagem',
            field=models.TextField(blank=True, null=True, verbose_name='Sua Mensagem'),
        ),
    ]