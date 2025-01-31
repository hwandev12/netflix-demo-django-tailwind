from django.db import models
from django.core.validators import FileExtensionValidator


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s janri" % self.name


class Film(models.Model):
    title = models.CharField(max_length=255)
    title_image = models.FileField(upload_to="films/title/", null=True)
    time = models.DurationField(blank=True, null=True)
    banner = models.ImageField(upload_to="films/banner/", null=True)
    card = models.ImageField(upload_to="films/card/", null=True)
    directors = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    description = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(auto_now_add=True)
    trailer = models.URLField()
    year = models.IntegerField()
    rating = models.FloatField(null=True)
    views = models.IntegerField(default=0, null=True)

    video_file = models.FileField(
        null=True,
        blank=True,
        upload_to="videos/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])],
    )

    is_movie = models.BooleanField(default=False)
    is_serie = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s)" % (self.title, self.year)


class FilmTrailer(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kino Trailerlari"
        verbose_name_plural = "Kino Trailerlari"
        indexes = [
            models.Index(fields=["film", "date_created"]),
        ]

    def __str__(self):
        return "%s" % self.film.title


# Series

class Episodes(models.Model):
    
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    time = models.DurationField()
    description = models.TextField()
    banner = models.ImageField(null=True, upload_to='series/banner/')
    
    class Meta:
        indexes = [
            models.Index(fields=['film', 'title'])
        ]
        
    def __str__(self):
        return "%s -- %s - %s" % (self.film.title, self.title, self.time)
    
    

