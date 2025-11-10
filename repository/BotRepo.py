import os
import psycopg2
from dotenv import load_dotenv

class BotRepo():
    
    def __init__(self):
        load_dotenv()
        self.database = os.getenv('POSTGRES_DB')
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = 5432
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
        sql = f'INSERT INTO member (username) values ({userName})'