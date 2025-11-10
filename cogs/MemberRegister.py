from discord.ext import commands

""" This Cog is responsible for managing the users that
have the movie watcher role """
class MemberRegister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repo = bot.repo

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        [print(role) for role in after.roles]

async def setup(bot):
    await bot.add_cog(MemberRegister(bot))
