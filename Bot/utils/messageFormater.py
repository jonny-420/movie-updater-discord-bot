import json

async def formatResponse(response):
    return [f"Title: {x[0]}, Description: {x[1]}, Release Date: {x[2]}" for x in response]