from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie
from .forms import MovieForm


# Create your views here.
# index: GET
# 전체 영화 데이터 조회 및 index.html 렌더링
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

# create: GET & POST
# create.html 렌더링
# 유효성 검증 및 영화 데이터 저장 후 detail.html 리다이렉트
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)

# detail: GET
# 단일 영화 데이터 조회 및 detail.html 렌더링
@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

# update: GET&POST
# 수정 대상 영화 데이터 조회 및 update.html 렌더링
# 유효성 검증 및 영화 데이ㅌ터 수정 후 detail.html 리다이렉트
@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

# delete: POST
# 단일 영화 데이터 삭제 및 index.html 리다이렉트
@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')
