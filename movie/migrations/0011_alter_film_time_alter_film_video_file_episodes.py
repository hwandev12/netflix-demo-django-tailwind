# Generated by Django 5.1.2 on 2025-01-22 10:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_filmtrailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='time',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DurationField()),
                ('description', models.TextField()),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.film')),
            ],
            options={
                'indexes': [models.Index(fields=['film', 'title'], name='movie_episo_film_id_8dac6c_idx')],
            },
        ),
    ]
