# Generated by Django 2.0.6 on 2018-07-05 02:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20180705_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='annual',
            field=models.BooleanField(verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='music',
            name='like_in',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(2017), django.core.validators.MaxValueValidator(2018)], verbose_name='在哪一年喜欢'),
        ),
    ]