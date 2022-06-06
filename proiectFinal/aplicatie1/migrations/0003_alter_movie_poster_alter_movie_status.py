# Generated by Django 4.0.4 on 2022-06-02 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0002_alter_movie_poster_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RECENTLY ADDED', 'RECENTLY ADDED'), ('MOST WATCHED', 'MOST WATCHED'), ('TOP RATED', 'TOP RATED')], max_length=20),
        ),
    ]
