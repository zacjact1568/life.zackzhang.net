# Generated by Django 2.0.6 on 2018-07-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20180712_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='you_tube',
            field=models.CharField(blank=True, max_length=100, verbose_name='YouTube'),
        ),
    ]
