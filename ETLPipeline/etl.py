import requests
import json
from dotenv import load_dotenv
import os
import psycopg2


def etl():
    load_dotenv()
    api_token = os.getenv('API_TOKEN')
    database = os.getenv('POSTGRES_DB')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {api_token}'
    }
    
    try:
        print(api_token)
        response = requests.get(url, headers=headers)
        print(response.text)
        upcoming = json.loads(response.text)['results']
        connection = psycopg2.connect(
            database = database,
            user = user,
            password = password,
            host = host,
            port = port
        )

        movie_query = "INSERT INTO movie (movie_id, title, overview, release_date, popularity) VALUES"
        genre_query = "INSERT INTO movie_genres (movie_id, genre_id) VALUES"
        for movie in upcoming:
            movie_query += f"({movie['id']}, '{movie['title']}', '{movie['overview']}', '{movie['release_date']}', {movie['popularity']}),"
            for genre in movie['genre_ids']:
                genre_query += f"({movie['id']}, {genre}),"  
        
        movie_query += movie_query[:-1] + ";"
        genre_query += genre_query[:-1] + ";"
        print(f"movie query: {movie_query}")
        print(f"genre query: {genre_query}")

        cursor = connection.cursor()
        cursor.execute(movie_query)
        cursor.execute(genre_query)
        connection.commit()
        connection.close()

    except psycopg2.DatabaseError as error:
        print(f"Something went wrong: \n{error}")                   

if __name__ == "__main__":
    print("I am about to run")
    etl()    # code to run when this file is executed directly

""" print("executed")
etl() """

