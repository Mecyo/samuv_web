# Generated by Django 2.0.7 on 2018-07-30 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_web', '0006_auto_20180730_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='dataHora',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 30, 2, 15, 26, 596635)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='foto',
            field=models.ImageField(upload_to='C:\\Users\\Mecyo\\Desktop\\SAMUV-PA\\samuv-web-master\\samuv_web\\images', verbose_name=models.CharField(default='IMG30072018021526', max_length=80)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG30072018021526', max_length=80),
        ),
    ]