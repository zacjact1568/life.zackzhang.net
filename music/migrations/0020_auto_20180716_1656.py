# Generated by Django 2.0.6 on 2018-07-16 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_auto_20180714_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='album_type',
        ),
        migrations.AlterField(
            model_name='music',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
        ),
    ]
