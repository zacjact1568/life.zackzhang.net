# Generated by Django 2.2.11 on 2020-03-28 12:08

from django.db import migrations, models
import django.db.models.deletion
import utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0031_auto_20200328_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_intro',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Intro'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_outro',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Outro'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_1',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 1'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_10',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 10'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_2',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 2'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_3',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 3'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_4',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 4'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_5',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 5'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_6',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 6'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_7',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 7'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_8',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 8'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='essentials_track_9',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='精选集 Track 9'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='song_of_this_year',
            field=models.ForeignKey(limit_choices_to={'essential': True, 'time__year': models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='music.Song', verbose_name='年度歌曲'),
        ),
        migrations.AlterField(
            model_name='annualsummary',
            name='year',
            field=models.IntegerField(default=utils.time.current_year, primary_key=True, serialize=False, verbose_name='年份'),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(default=utils.time.current_year, verbose_name='年份'),
        ),
    ]
