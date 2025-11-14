import os
from dotenv import load_dotenv
import requests


class HttpService():
    
    def __init__(self):
        load_dotenv()
        self.api_token = os.getenv('API_TOKEN')    

    """ TODO: the requests library performs synch requests, change for
    another library to perform async requests """ 
    async def fecthUpcoming(self): 
        print(self.api_token)
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f'Bearer {self.api_token}'
        }

        response = requests.get(url, headers=headers) 
        print(response)
        return response