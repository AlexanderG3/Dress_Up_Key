# Generated by Django 3.1.2 on 2020-10-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_auto_20201016_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Entregado', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Envio',
                'verbose_name_plural': 'Envios',
            },
        ),
    ]
