# Generated by Django 2.2.11 on 2020-04-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200413_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='标签'),
        ),
    ]
