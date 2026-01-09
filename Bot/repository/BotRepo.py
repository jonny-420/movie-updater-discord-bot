import os
import psycopg2
from dotenv import load_dotenv
import bcrypt
from Exceptions.SubscriptionViolationException import SubscriptionViolationException

class BotRepo():
    
    def __init__(self):
        load_dotenv()
        self.database = os.getenv('POSTGRES_DB')
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.connection = None

    def connect(self):
        if(self.connection != None):
            return
        
        print("starting Connection")
        self.connection = psycopg2.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )

    def disconnect(self):
        if(self.connection == None):
            return
        
        self.connection.close()

    def insertMember(self, userId, userName):
        cursor = self.connection.cursor()
        hashedId = self.__hashId(userId) 
        sql = f"INSERT INTO member (id, username) VALUES ('{hashedId}' , '{userName}')"
        cursor.execute(sql)
        self.connection.commit()

    # TODO: Rethink if it's better to remove based on user id rather than his name.
    def removeMember(self, userName):
        cursor = self.connection.cursor()
        sql = f'DELETE FROM member WHERE username = \'{userName}\''
        cursor.execute(sql)
        self.connection.commit()

    def getGenres(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM genres"
        cursor.execute(sql)
        response = cursor.fetchall()
        print(response)
        return response
        
    # TODO: missing validation to prevent a user from subscribing more than once to the same genre
    def insertGenreSubscription(self, genre, member):
        try:
            cursor = self.connection.cursor()
            member_id = self.getMemberId(cursor, member)      # This step already fetches the hashed member id from the database
            # print(member_id)
            sql = f"INSERT INTO genre_subscription (genre_id, member_id) VALUES ({genre[0]}, '{member_id}')"
            cursor.execute(sql)
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            raise SubscriptionViolationException()
        except psycopg2.DatabaseError as error:
            self.connection.rollback()
            print(error)

    def listSubscriptions(self, member):
        try:
            cursor = self.connection.cursor()
            member_id = self.getMemberId(cursor, member)
            sql = f"SELECT genres.genre_id, genres.genre FROM genres JOIN genre_subscription ON genres.genre_id = genre_subscription.genre_id WHERE genre_subscription.member_id = '{member_id}'"
            cursor.execute(sql)
            return cursor.fetchall()
        except psycopg2.DatabaseError as error:
            self.connection.rollback()
            print(f"Error listing subscriptions: \n{error}")

    # Function that allows to fetch the hased member id from the database
    def getMemberId(self, cursor, member):
        sql = f"SELECT id FROM member WHERE username = '{member.name}'"
        cursor.execute(sql)
        return cursor.fetchall()[0][0]
    
    def upcomingMoviesBySubscription(self, member):
        try:
            cursor = self.connection.cursor()
            member_id = self.getMemberId(cursor, member)
            sql = f"SELECT movie.title, movie.overview, movie.release_date FROM genre_subscription JOIN movie_genres ON genre_subscription.genre_id = movie_genres.genre_id JOIN movie ON movie.movie_id = movie_genres.movie_id WHERE member_id = '{member_id}' AND movie.release_date >= DATE(now())"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as error:
            print(f"Error returning the movie list based on user subscribed genres: \n{error}")


    # Auxiliar function to hash user ids
    def __hashId(self, userId):
        bytes = str(userId).encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        return hash.decode('utf-8')