# Generated by Django 4.0.4 on 2022-06-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0003_alter_movie_poster_alter_movie_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
