# Generated by Django 2.0.7 on 2018-07-29 22:16

import datetime
from django.db import migrations, models
import samuv_web.models


class Migration(migrations.Migration):

    dependencies = [
        ('samuv_web', '0003_auto_20180729_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caracteristica_da_ferida',
            options={'verbose_name': 'Característica da ferida', 'verbose_name_plural': 'Característica das feridas'},
        ),
        migrations.AlterModelOptions(
            name='imagem',
            options={'verbose_name': 'Imagem', 'verbose_name_plural': 'Imagens'},
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='dataHora',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 19, 16, 27, 810774)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='foto',
            field=models.ImageField(upload_to=samuv_web.models.get_image_path, verbose_name=models.CharField(default='IMG<django.db.models.fields.related.ForeignKey><built-in method now of type object at 0x00007FFAB12F3D60>', max_length=80)),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageName',
            field=models.CharField(default='IMG<django.db.models.fields.related.ForeignKey><built-in method now of type object at 0x00007FFAB12F3D60>', max_length=80),
        ),
    ]