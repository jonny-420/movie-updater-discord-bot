import requests
import json
from dotenv import load_dotenv
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BIGINT, Integer, ForeignKey, String, Date, REAL 


Base = declarative_base()

class movie(Base):
    __tablename__ = "movie"
    movie_id = Column(BIGINT, primary_key=True)
    title = Column(String)
    overview = Column(String)
    release_date = Column(Date)
    popularity = Column(REAL)

class genres(Base):
    __tablename__ = "genres"
    genre_id = Column(BIGINT, primary_key=True)
    genre = Column(String)

class movieGenre(Base):
    __tablename__ = "movie_genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(BIGINT, ForeignKey('movie.movie_id'))
    genre_id = Column(BIGINT, ForeignKey("genres.genre_id"))



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
        # First step is to get the movies from the TMDB API
        print(api_token)
        response = requests.get(url, headers=headers)
        print(response.text)
        upcoming = json.loads(response.text)['results']

        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{database}")
        session = sessionmaker(bind = engine)
        connection = session()

        movie_query = []                               # "INSERT INTO movie (movie_id, title, overview, release_date, popularity) VALUES"
        genre_query = []                                  # "INSERT INTO movie_genres (movie_id, genre_id) VALUES"
        for m in upcoming:
            movie_query.append(movie(movie_id = m['id'], title = m['title'], overview = m['overview'], release_date = m['release_date'], popularity = m['popularity']))  
            for genre in m['genre_ids']:
                genre_query.append(movieGenre(movie_id = m['id'], genre_id = genre))   
        
        """ movie_query += movie_query[:-1] + ";" 
        genre_query += genre_query[:-1] + ";"
        print(f"movie query: {movie_query}")
        print(f"genre query: {genre_query}")

        cursor = connection.cursor()
        cursor.execute(movie_query)
        cursor.execute(genre_query) """
        
        connection.add_all(movie_query)
        connection.add_all(genre_query)
        connection.commit()
        
    except psycopg2.DatabaseError as error:
        print(f"Something went wrong: \n{error}")    
    finally:
        connection.close()

if __name__ == "__main__":
    print("I am about to run")
    etl()    # code to run when this file is executed directly

""" print("executed")
etl() """

