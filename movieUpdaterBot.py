import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from services.httpService import fecthUpcoming
from services.messageFormater import formatResponse
from repository.BotRepo import BotRepo
from services.getRolesNames import get_roles_names


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
botRepo = BotRepo()
bot.repo = botRepo


async def check_user_role(ctx):
    member = ctx.author
    user_roles = get_roles_names(member.roles)
    if "movie watcher" in user_roles:
        return True
    await ctx.send('You don\'t have the necessary role to use this bot')
    return False

@bot.command()
@commands.check(check_user_role) 
async def ping(ctx):
    await ctx.send("I am alive")

# TODO: DO a help command later
""" @bot.command()
async def help(ctx):
    await ctx.send("help") """

@bot.command()
@commands.check(check_user_role)
async def listCommands(ctx):
    await ctx.send("/ping -> checks if the bot is alive \n"
    "/subscribe genre -> subscribe to topics of a specific genre\n"
    "/list genres -> lists all the genres that a user is subscribed to\n"
    "/unsubscribe genre -> allows a user to unsubscribe to a genre\n")

@bot.command()
@commands.check(check_user_role)
async def upcoming(ctx):
    try:
        response = await fecthUpcoming()
        ans = await formatResponse(response)
        [await ctx.send(movie) for movie in ans]
    except:
        await ctx.send('Something Went wrong ;-; Please try again later.')
    # print(response.text)


@bot.command()
@commands.check(check_user_role)
async def subscribe(ctx):
    member = ctx.author
    print(f'member id: {member.id}, member name: {member.name}')

@bot.event
async def on_ready():
    bot.repo.connect()
    await bot.load_extension("cogs.MemberRegister")
    print("loaded cog")

bot.run(token)