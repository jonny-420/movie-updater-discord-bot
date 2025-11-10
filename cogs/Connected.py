from discord.ext import commands


""" This class will register the bot connection events.
Most specifically the connected and disconected to 
open and close the db connections. """
class Connected(commands.cog):

    def __init__(self, botRepo):
        self.botRepo = botRepo

    @commands.Cog.listener()
    async def on_connect(self):
        self.botRepo.connect()