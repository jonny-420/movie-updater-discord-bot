from discord.ext import commands
from services.getRolesNames import get_roles_names

""" This Cog is responsible for managing the users that
have the movie watcher role """
class MemberRegister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repo = bot.repo

    # TODO: try to make this function more eficient
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        after_roles_names = get_roles_names(after.roles) 
        before_roles_names = get_roles_names(before.roles) 
        if "movie watcher" in after_roles_names:
            if "movie watcher" in before_roles_names:
                return
            self.repo.insertMember(after.id, after.name)
        else:
            if "movie watcher" not in before_roles_names:
                return
            self.repo.removeMember(after.name)


async def setup(bot):
    await bot.add_cog(MemberRegister(bot))
