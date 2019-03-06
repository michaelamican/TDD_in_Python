from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

def add(request):
    if request.method == 'POST':
        # spread operator in Python
        # Album.objects.create(**request.POST)
        Album.objects.create(title =title.request.POST['title'], artist =
        request.POST['artist'], year = request.POST['year'])
    return redirect('/')

def edit(request):
    context = {
        "album" : Album.objects.get(id = 1)
    }
    return render(requst, "index.html", context)

def delete(request):
    return redirect('/')