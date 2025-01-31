from django.contrib import admin
from . import models

MODELS = [
    models.User, models.AccountCard
]

for _ in MODELS:
    admin.site.register(_)
