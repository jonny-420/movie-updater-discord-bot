import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from httpService import fecthUpcoming
from messageFormater import formatResponse

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

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
async def listCommands(ctx):
    await ctx.send("/ping -> checks if the bot is alive \n"
    "/subscribe genre -> subscribe to topics of a specific genre\n"
    "/list genres -> lists all the genres that a user is subscribed to\n"
    "/unsubscribe genre -> allows a user to unsubscribe to a genre\n")

@bot.command()
async def upcoming(ctx):
    try:
        response = await fecthUpcoming()
        ans = await formatResponse(response)
        [await ctx.send(movie) for movie in ans]
    except:
        await ctx.send('Something Went wrong ;-; Please try again later.')
    # print(response.text)


""" @bot.command()
async def subsrcibe(ctx): """

bot.run(token)