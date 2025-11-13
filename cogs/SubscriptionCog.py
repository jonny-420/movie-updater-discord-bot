from discord.ext import commands
from services.checkUserRoles import check_user_role

class SubscriptionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repo = bot.repo

    """ This command will allow other types od subscriptions.
For now it is only being considered genre subsrciptions """
    @commands.command()
    @commands.check(check_user_role)
    async def subscribe(self, ctx, arg):
        match arg:
            case "genre":
                member = ctx.author
        await ctx.send("funciona como tu pensas mano")
        # print(f'member id: {member.id}, member name: {member.name}')

async def setup(bot):
    await bot.add_cog(SubscriptionCog(bot))