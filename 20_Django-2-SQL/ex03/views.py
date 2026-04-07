from django.shortcuts import render, HttpResponse
from ex03.models import Movies


def populate(request):
    results = []
    try:
        movies = [
            ("The Phantom Menace", 1, "", "George Lucas", "Rick McCallum", "1999-05-19"),
            ("Attacks of the Clones", 2, "", "George Lucas", "Rick McCallum", "2002-05-16"),
            ("Revenge of the Sith", 3, "", "George Lucas", "Rick McCallum", "2005-05-19"),
            ("A New Hope", 4, "", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-12"),
            ("The Empire Strikes Back", 5, "", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
            ("Return of the Jedi", 6, "", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
            ("The Force Awakens", 7, "", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
        ]

        for m in movies:
            Movies.objects.update_or_create(
                episode_nb=m[1], 
                defaults={
                    'title': m[0],
                    'opening_crawl': m[2],
                    'director': m[3],
                    'producer': m[4],
                    'release_date': m[5]
                }
            )
            results.append("OK")

        return HttpResponse("<br>".join(results))
    
    except Exception as e:
        return HttpResponse(f"Error : {e}")

def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available.")
        return render(request, "ex03/display.html", {"movies": movies})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
