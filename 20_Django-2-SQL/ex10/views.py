from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
from .forms import CharacterSearchForm
from .models import People

def form_view(request):
    characters = []
    form = CharacterSearchForm()
    if request.method == 'POST':
        form = CharacterSearchForm(request.POST)
        if form.is_valid():
            min_date = form.cleaned_data["min_date"]
            max_date = form.cleaned_data["max_date"]
            diameter = form.cleaned_data["diameter"]
            gender = form.cleaned_data["gender"]

            result = People.objects.filter(
                gender=gender,
                homeworld__diameter__gt=diameter,
                movies__release_date__range=(min_date, max_date)
            ).values(
                'name',
                'gender',
                'movies__title',
                'homeworld__name',
                'homeworld__diameter'
            ).order_by('name')    
            characters = list(result)
            form = CharacterSearchForm()

    return render(request, 'ex10/index.html', { 'form': form, 'characters': list(characters) })
