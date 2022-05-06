from django.shortcuts import render
from django.views.decorators.http import require_safe, require_GET
from django.shortcuts import get_object_or_404

from .models import Movie


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.order_by('-popularity')[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)