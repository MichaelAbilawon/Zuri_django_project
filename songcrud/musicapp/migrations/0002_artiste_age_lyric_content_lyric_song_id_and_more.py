# Generated by Django 4.1.2 on 2022-10-28 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lyric',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
