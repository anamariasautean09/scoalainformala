# Generated by Django 4.0.4 on 2022-06-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1500)),
                ('release_date', models.CharField(max_length=15)),
                ('duration', models.CharField(max_length=10)),
                ('budget', models.CharField(max_length=25)),
                ('rating', models.FloatField()),
                ('poster', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE'), ('adventure', 'ADVENTURE'), ('love', 'LOVE'), ('cartoons', 'CARTOONS')], max_length=12)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN'), ('spanish', 'SPANISH')], max_length=12)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
