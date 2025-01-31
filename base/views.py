from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

from movie.models import Film
from django.utils import timezone

def home(request):
    language = Addlanguage.objects.all()
    return render(request, 'welcome.html', {'language': language})


def main(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    main_film = Film.objects.filter(created_at__lte=timezone.now(), rating__gte=8).exists()
    if main_film:
        main_film = Film.objects.filter(created_at__lte=timezone.now(), rating__gte=8).first()
    else:
        main_film = None
    one_week_ago = timezone.now() - timezone.timedelta(days=7)
    new_this_week = Film.objects.filter(created_at__gte=one_week_ago, created_at__lte=timezone.now()).order_by('-created_at')
    trending_movies = Film.objects.filter(created_at__gte=one_week_ago, created_at__lte=timezone.now(), views__gte=1000).order_by('-views')
    return render(request, 'main.html', { 'films': new_this_week, 'main_film': main_film, 'trending_movies': trending_movies })
