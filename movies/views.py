from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre


# Create your views here.
# Declare functions that take inputs from client
# performs processing and returns to the client

def index(request):
    # Movie.objects.all() - reads the table
    # Movie.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)

    catalog = Movie.objects.all()
    return render(request,"views/index.html",{"catalog": catalog})

def test(request):
    return HttpResponse("<h1>Im a Test</h1>")

def contact(request):
    return HttpResponse("<h2>Page under construction</h2>")

