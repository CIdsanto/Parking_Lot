# Generated by Django 4.0 on 2021-12-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_estatus_alter_clientes_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='entrada',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Entrada'),
        ),
    ]
