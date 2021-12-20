# Generated by Django 4.0 on 2021-12-20 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espacios', models.IntegerField(verbose_name='Espacios Totales')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=120, verbose_name='Numero Placa')),
                ('entrada', models.DateTimeField(blank=True, null=True, verbose_name='Entrada')),
                ('salida', models.DateTimeField(blank=True, null=True, verbose_name='Salida')),
                ('pago', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(max_length=1, null=True)),
                ('slot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.size')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.tipo')),
            ],
        ),
    ]
