from django.db import models
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
    ('adventure', 'ADVENTURE'),
    ('love', 'LOVE'),
    ('cartoons', 'CARTOONS'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('german', 'GERMAN'),
    ('spanish', 'SPANISH'),
)

STATUS_CHOICES = (
    ('RECENTLY ADDED', 'RECENTLY ADDED'),
    ('MOST WATCHED', 'MOST WATCHED'),
    ('TOP RATED', 'TOP RATED'),
)
class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    release_date = models.DateField()
    duration = models.CharField(max_length=10)
    budget = models.CharField(max_length=25)
    rating = models.FloatField()
    poster = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=12)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=12)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    trailer_url = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=1)


    def __str__(self):
        return f"{self.title} - {self.description} - {self.release_date} - {self.duration} - {self.budget} - {self.category} - {self.description} - {self.language} - {self.status}"
