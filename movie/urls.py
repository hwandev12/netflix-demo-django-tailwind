from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:film_id>/', views.film_detail, name='film_detail'),
]