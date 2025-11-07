import os

import discord
from discord.ext import commands

from dotenv import load_dotenv
import requests
import json

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
api_token = os.getenv('API_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("I am alive")

# TODO: DO a help command later
""" @bot.command()
async def help(ctx):
    await ctx.send("help") """


@bot.command()
async def upcoming(ctx):
    try:
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f'Bearer {api_token}'
        }

        response = requests.get(url, headers=headers)
        # print(response.text)
        ans = await formatResponse(response)
        [await ctx.send(movie) for movie in ans]
    except:
        await ctx.send('Something Went wrong ;-; Please try again later.')
    # print(response.text)


async def formatResponse(response):
    
    return [f"Title: {x['title']}, Release Date: {x['release_date']}, description: {x['overview']}" 
        for x in json.loads(response.text)['results']]
    

bot.run(token)