# Generated by Django 2.0.6 on 2018-07-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20180705_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='annual',
        ),
        migrations.RemoveField(
            model_name='music',
            name='like_in',
        ),
    ]
