from django.shortcuts import HttpResponse
from django.conf import settings
import psycopg2

def init(request):
    db_config = settings.DATABASES['default']

    try:
        connection = psycopg2.connect(
            dbname=db_config['NAME'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT']
        )
        cur =connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
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
    except OperationalError as e:
        return HttpResponse(f"Error connecting to the Database: {e}")

    except Error as e:
        return HttpResponse(f"Error SQL : {e}")
