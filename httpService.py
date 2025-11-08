import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_token = os.getenv('API_TOKEN')

async def fecthUpcoming(): 
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {api_token}'
    }

    return requests.get(url, headers=headers)