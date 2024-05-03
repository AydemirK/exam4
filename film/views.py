from django.shortcuts import render, get_object_or_404
from django.db import models

from film.models import Film, Actor, Genre


def main_view(request):
    return render(request, "main.html")


def film_list_view(request):
    films = Film.objects.all()
    return render(request, "films/list.html", {"films": films})


def film_detail_view(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return render(request, "errors/404.html")
    
    return render(request, "films/detail.html", {"film": film})


def actor_list_view(request):
    
    actors = Actor.objects.all().annotate(rating=models.Avg("films__rating")).order_by("-rating")

    return render(request, "actors/list.html", {"actors": actors})


def actor_detail_view(request, actor_id):

    actor = get_object_or_404(Actor, id=actor_id)

    return render(request, 'actors/actor_detail.html', {'actor': actor})
