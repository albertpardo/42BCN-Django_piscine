from django.shortcuts import render, HttpResponse
from django.conf import settings
import psycopg2

def _connection_data():
    db_config = settings.DATABASES['default']
    return psycopg2.connect(
        dbname=db_config['NAME'],
        user=db_config['USER'],
        password=db_config['PASSWORD'],
        host=db_config['HOST'],
        port=db_config['PORT']
    )

def init(request):

    try:
        connection =  _connection_data()
        cur =connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_Date DATE NOT NULL
                )
                """)
        connection.commit()
        cur.close()
        connection.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error SQL : {e}")

def populate(request):
    db_config = settings.DATABASES['default']

    try:
        connection =  _connection_data()
        cur =connection.cursor()

        cur.execute("TRUNCATE TABLE ex04_movies RESTART IDENTITY;")
        movies = [
            ("The Phantom Menace", 1, "", "George Lucas", "Rick McCallum", "1999-05-19"),
            ("Attacks of the Clones", 2, "", "George Lucas", "Rick McCallum", "2002-05-16"),
            ("Revenge of the Sith", 3, "", "George Lucas", "Rick McCallum", "2005-05-19"),
            ("A New Hope", 4, "", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-12"),
            ("The Empire Strikes Back", 5, "", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
            ("Return of the Jedi", 6, "", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
            ("The Force Awakens", 7, "", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
        ]
        context = []
        for movie in movies:
            cur.execute("""
                    INSERT INTO ex04_movies (title, episode_nb, opening_crawl, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, movie)
            context.append("OK")

        connection.commit()
        cur.close()
        connection.close()

        return HttpResponse("<br>".join(context))
    
    except Exception as e:
        return HttpResponse(f"Error SQL : {e}")

def display(request):
    db_config = settings.DATABASES['default']

    try:
        connection =  _connection_data()
        cur = connection.cursor()
        cur.execute("SELECT * FROM ex04_movies;")
        movies = cur.fetchall()
        cur.close()
        connection.close()
        if not movies:
            raise Exception("No data available")
        movies_dic = []
        for movie in movies:
            movies_dic.append({
                'title': movie[0],
                'episode_nb': movie[1],
                'opening_crawl': movie[2],
                'director': movie[3],
                'producer': movie[4],
                'release_date': movie[5]
                }
            )
        return render(request, 'ex04/display.html', {'movies': movies_dic})
    except Exception as e:
        return HttpResponse(f"Error: '{e}'")


def remove(request):

    try:
        connection =  _connection_data()
        cur = connection.cursor()

        if request.method == "POST":
            title = request.POST.get("title")
            print(title)
            if title:
                cur.execute("DELETE FROM ex04_movies WHERE title = %s", [title])
                connection.commit()

        cur.execute("SELECT title FROM ex04_movies;")
        titles = [row[0] for row in cur.fetchall()]

        cur.close()
        connection.close()
        return render(request, 'ex04/remove.html', {'titles': titles})
    except Exception as e:
        return HttpResponse(f"Error: '{e}'")
