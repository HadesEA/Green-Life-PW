# Generated by Django 5.1.3 on 2024-12-05 23:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_counter_counterdistancia_counterht_counterlluvia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_riego', models.DateField(default=django.utils.timezone.now)),
                ('tiempo_riego', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cosecha',
            name='tiempo_cosecha',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='insumo',
            name='fecha_insumo',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='insumo',
            name='tiempo_insumo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='siembra',
            name='tiempo_siembra',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cosecha',
            name='fecha_cosecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='siembra',
            name='fecha_siembra',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]