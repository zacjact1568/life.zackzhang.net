# Generated by Django 2.2.9 on 2020-02-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0026_auto_20190430_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='essential',
            field=models.SmallIntegerField(choices=[(-1, '否'), (0, 'Intro'), (1, 'Track 1'), (2, 'Track 2'), (3, 'Track 3'), (4, 'Track 4'), (5, 'Track 5'), (6, 'Track 6'), (7, 'Track 7'), (8, 'Track 8'), (9, 'Track 7'), (10, 'Track 10'), (11, 'Outro')], default=-1, verbose_name='精选'),
        ),
    ]
