# Generated by Django 5.1.2 on 2024-12-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_film_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
