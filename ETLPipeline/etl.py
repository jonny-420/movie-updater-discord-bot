import requests
import json
from dotenv import load_dotenv
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DTOS import movie, movieGenre
from publisher import publisher
import pika

def etl():
    load_dotenv()
    api_token = os.getenv('API_TOKEN')
    database = os.getenv('POSTGRES_DB')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('DB_HOST')
    rabbit_host = os.getenv('RABBIT_HOST')
    rabbit_pwd = os.getenv('RABBITMQ_DEFAULT_PASS')
    rabbit_usr = os.getenv('RABBITMQ_DEFAULT_USER')
    exchange_name = os.getenv('EXCHANGE_NAME') 
    routing_key = os.getenv('ROUTING_KEY')
    rabbit_port = os.getenv('RABBIT_PORT')
    

    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {api_token}'
    }
    p = publisher(exchange_name, routing_key, rabbit_usr, rabbit_pwd, rabbit_port, rabbit_host)

    try:
        # First step is to get the movies from the TMDB API
        response = requests.get(url, headers=headers)
        upcoming = json.loads(response.text)['results']

        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{database}")
        session = sessionmaker(bind = engine)
        connection = session()
        p.connect()
        # The second step is to create te objects to be inserted on the database
        movie_query = []                               # "INSERT INTO movie (movie_id, title, overview, release_date, popularity) VALUES"
        genre_query = []                                  # "INSERT INTO movie_genres (movie_id, genre_id) VALUES"
        for m in upcoming:
            movie_query.append(movie(movie_id = m['id'], title = m['title'], overview = m['overview'], release_date = m['release_date'], popularity = m['popularity']))  
            for genre in m['genre_ids']:
                genre_query.append(movieGenre(movie_id = m['id'], genre_id = genre))   
        
        connection.add_all(movie_query)
        connection.add_all(genre_query)
        connection.commit()
        p.publish(movie_query)
    except psycopg2.DatabaseError as error:
        print(f"Something went wrong: \n{error}")  
    except pika.exceptions.AMQPConnectionError as e:
        print(f"AMQP Connection Error: \n{e}")
    finally:
        connection.close()
        p.disconnect()

if __name__ == "__main__":
    etl()    



