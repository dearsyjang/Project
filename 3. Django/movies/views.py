from django.shortcuts import render
import requests
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/278/recommendations'
    parmas = {
        'api_key' : '423115a7b5585375b2590b4770f1a0b9',
        'language': 'ko',
    }
    response = requests.get(BASE_URL+path,params=parmas)
    data = response.json()
    movie_list = data.get('results')
    return movie_list

def recommendations(request):
    movielist = recommendation('쇼생크 탈출')
    choice_movie = random.choice(movielist)
    title = choice_movie['title']
    overview = choice_movie['overview']
    release_date = choice_movie['release_date']
    vote_average = round(choice_movie['vote_average'], 1)
    poster_path = choice_movie['poster_path']
    movie_id = choice_movie['id']
    
    context = {
        'movielist' : movielist,
        'choice_movie' : choice_movie,
        'title' : title,
        'overview' : overview,
        'release_date' :release_date,
        'vote_average' : vote_average,
        'poster_path' : poster_path,
        'movie_id' : movie_id,
    }
    return render(request,'recommendations.html',context)