from django.shortcuts import render
from django.http import HttpResponse
from .models import People


def display(request):
    try:
        people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name').select_related('homeworld')
        if not people:
            return HttpResponse("No data available, please use the following command line before use: python3 manage.py loaddata ex09_initial_data.json")
        return render(request, "ex09/display.html", {"people": people})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
