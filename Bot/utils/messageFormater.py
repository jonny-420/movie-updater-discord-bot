import json

async def formatResponse(response):
    return [f"Title: {x['title']}, Release Date: {x['release_date']}, description: {x['overview']}" 
        for x in json.loads(response.text)['results']]