# Generated by Django 2.0.7 on 2018-07-30 05:06

import datetime
from django.db import migrations, models
import samuv_web.models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_web', '0005_auto_20180730_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='dataHora',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 30, 2, 6, 28, 351074)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='foto',
            field=models.ImageField(upload_to=samuv_web.models.get_image_path, verbose_name=models.CharField(default='IMG30072018020628', max_length=80)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG30072018020628', max_length=80),
        ),
    ]