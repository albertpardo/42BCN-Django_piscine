from django.shortcuts import render, HttpResponse
from django.conf import settings
import psycopg2
from psycopg2.extras import DictCursor

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
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(255),
                diameter INT,
                orbital_period INT,
                population bigINT,
                rotation_period INT,
                surface_water REAL,
                terrain VARCHAR(128)
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
            )
        """)

        connection.commit()
        cur.close()
        connection.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error SQL : {e}")

def populate(request):
    try:
        results = []
        planets_path = settings.BASE_DIR / 'planets.csv'
        people_path = settings.BASE_DIR / 'people.csv'

        connection =  _connection_data()
        cur = connection.cursor()
        
        cur.execute("TRUNCATE TABLE ex08_planets, ex08_people  RESTART IDENTITY;")
   
        with open(planets_path, 'r') as f:
            cur.copy_expert("""
                COPY ex08_planets(name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                FROM STDIN WITH (FORMAT CSV, DELIMITER '\t', NULL 'NULL')
            """, f)
        results.append("OK.")
        with open(people_path, 'r') as f:
            cur.copy_expert("""
                COPY ex08_people(name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                FROM STDIN WITH (FORMAT CSV, DELIMITER '\t', NULL 'NULL')
            """, f)
        connection.commit()
        cur.close()
        connection.close()
        
        results.append("</br>OK.")
        return HttpResponse(results)
    except Exception as e:
        return HttpResponse(f"Error SQL : {e}")

def display(request):
    try:
        connection =  _connection_data()
        cur =connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT people.name, people.homeworld, planets.climate
            FROM ex08_people people
            JOIN ex08_planets planets
            ON people.homeworld = planets.name
            WHERE planets.climate LIKE '%windy%'
            ORDER BY people.name ASC
        """)
        people = cur.fetchall()

        connection.commit()
        cur.close()
        connection.close()
        if not people:
            return HttpResponse("No data available.")
        return render(request, 'ex08/display.html', {'people': people})

    except Exception as e:
        return HttpResponse(f"Error: '{e}'")
