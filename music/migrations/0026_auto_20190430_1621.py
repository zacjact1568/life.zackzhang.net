# Generated by Django 2.0.6 on 2019-04-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0025_auto_20190430_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.CharField(max_length=100, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='music',
            name='link',
            field=models.CharField(blank=True, max_length=100, verbose_name='链接'),
        ),
    ]
