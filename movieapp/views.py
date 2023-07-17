from django.shortcuts import render

# Create your views here.

import operator
from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
# from recommender.recommendations import load_recommendations
from functools import reduce
from django.db.models import Q


def search_movies(request):
    query = request.get('search_query')
    movies = Movie.objects.all()
    query_elements = query.split()
    filtered = movies.filter(reduce(operator.and_,(Q(title__icontains=q) for q in query_elements)))
    return {'search_results': filtered}


def home(request):
    if request.method == 'GET' and len(request.GET) > 0:
        search_results = search_movies(request.GET)
        return render(request, 'home.html', context=search_results)

    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'home' : 'active'
    }
    return render(request, 'home.html', context = context)




def about(request):
    context = {
        'about' : 'active',
    }
    return render(request, 'about.html', context=context)