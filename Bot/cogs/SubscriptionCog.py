from discord.ext import commands
from services.checkUserRoles import check_user_role
from services.subscribeService import SubscriptionService

class SubscriptionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = SubscriptionService(bot.repo, bot)

    """ This command will allow other types od subscriptions.
For now it is only being considered genre subsrciptions """
    @commands.command()
    @commands.check(check_user_role)
    async def subscribe(self, ctx, arg):
        try:
            match arg:
                case "genre":
                    await self.service.subscribeByGenre(ctx)
                    # member = ctx.author
                case "company":
                    member = ctx.author
                case _:
                    await ctx.send("Please select one of the available subscription types: genre, company")
        except:
            await ctx.send("You must send only one of the following valid args: genre, company")
        
        # print(f'member id: {member.id}, member name: {member.name}')

    @commands.command()
    @commands.check(check_user_role)
    async def listSubscriptions(self, ctx):
        await self.service.listSubscriptions(ctx)

async def setup(bot):
    await bot.add_cog(SubscriptionCog(bot))