# Generated by Django 2.0.6 on 2018-07-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20180709_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='source',
            field=models.CharField(max_length=100, verbose_name='来源'),
        ),
    ]