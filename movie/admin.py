from django.contrib import admin
from . import models

MODELS = [
    models.Genre,
    models.Film,
    models.FilmTrailer,
    models.Episodes
]

for _ in MODELS:
    admin.site.register(_)
