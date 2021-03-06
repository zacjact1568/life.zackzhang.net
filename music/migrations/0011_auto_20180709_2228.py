# Generated by Django 2.0.6 on 2018-07-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20180709_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='source_type',
            field=models.CharField(choices=[('apple_music', 'Apple Music'), ('spotify', 'Spotify'), ('netease_cloud_music', '网易云音乐'), ('qq_music', 'QQ 音乐')], default='apple_music', max_length=20, verbose_name='来源类型'),
        ),
    ]
