from django.shortcuts import render, redirect
from .models import *


def film_detail(request, film_id):
    if not request.user.is_authenticated:
        return redirect("/auth/login")
    try:
        film = Film.objects.get(id=film_id)
        related_films = (
            Film.objects.all()
            .filter(genre__in=film.genre.all().values_list("id", flat=True))
            .exclude(id=film.id)
            .distinct()
        )
        trailers = FilmTrailer.objects.filter(film=film)
        
        # episodni olish
        indexes_array = [1, 2, 3]
        indexes = 0
        episodes = Episodes.objects.filter(film=film)
        for _ in episodes:
            indexes += 1  
            indexes_array.append(indexes)
        
        full_episodes = zip(indexes_array, episodes)
        
        # zip([1, 2, 3, 4], episodelar)
        
    except (Film.DoesNotExist, FilmTrailer.DoesNotExist):
        print("Error")

    return render(
        request, "film_detail.html", {"film": film, "related_films": related_films, 'trailers': trailers, "episodes": full_episodes}
    )
