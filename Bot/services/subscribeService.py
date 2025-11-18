
class SubscriptionService():

    def __init__(self, repo):
        self.repo = repo

    async def subscribeByGenre(self, ctx):
        try:
            await self.repo.getGenres()
            while True:
                await ctx.send("please select one of the following genres:")
        except:
            ctx.send("Timeout exceeded")
    
