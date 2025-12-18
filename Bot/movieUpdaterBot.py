import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from services.httpService import HttpService
from repository.BotRepo import BotRepo
from services.checkUserRoles import check_user_role
from services.consumer import consumer

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
rabbit_user = os.getenv('RABBITMQ_DEFAULT_USER')
rabbit_pwd = os.getenv('RABBITMQ_DEFAULT_PASS')
exchange_name = os.getenv('EXCHANGE_NAME')
routing_key = os.getenv('ROUTING_KEY')
rabbit_host = os.getenv('RABBIT_HOST')
rabbit_port = os.getenv('RABBIT_PORT')
channel_id = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
botRepo = BotRepo()
bot.repo = botRepo
service = HttpService()
consumer = consumer(exchange_name, routing_key, rabbit_user, rabbit_pwd, rabbit_port, rabbit_host, bot, channel_id)

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


@bot.event
async def on_ready():
    bot.repo.connect()
    await bot.load_extension("cogs.MemberRegister")
    await bot.load_extension("cogs.SubscriptionCog")
    await consumer.connect()
    bot.loop.create_task(consumer.consume())
    print("loaded cog")

bot.run(token)