# Generated by Django 5.1.3 on 2024-11-20 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertasUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacion', models.BooleanField(default=False)),
                ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.alertas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
    ]