# films/views.py
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Представление для добавления фильма
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

# Представление для отображения списка фильмов
def index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', {'films': films})

