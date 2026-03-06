from utils.formatGenreList import formatGenreList
from Exceptions.SubscriptionViolationException import SubscriptionViolationException


class SubscriptionService():

    def __init__(self, repo, bot):
        self.repo = repo
        self.bot = bot

    async def subscribeByGenre(self, ctx):
        try:
            res = await self.repo.getGenres()
            msg = formatGenreList(res)
            
            await ctx.send(f'please select one of the following genres:\n {msg}')

            while True:
                def validate(i):
                    return i.author == ctx.author and i.channel == ctx.channel
                
                choice = await self.bot.wait_for('message', check=validate, timeout=60.0)
                choice = int(choice.content) 
                if choice >= 0 and choice <= len(res):
                    print(choice)
                    self.repo.insertGenreSubscription(res[choice], ctx.author)
                    await ctx.send(f"successfully subscribed to {res[choice][1]}")
                    break
                else:
                    await ctx.send("please select a valid number")   

        except SubscriptionViolationException:
            await ctx.send("You're already subscribed to that genre")
        except Exception as e:
            message = str(e)           
            print(f"Error: {message}")        
            await ctx.send("Something went wrong, please try again later!")

    async def listSubscriptions(self, ctx):
        try:
            genres = self.repo.listSubscriptions(ctx.author)
            print(genres)
            msg = formatGenreList(genres)
            await ctx.send(f"{ctx.author} doesn't have any subscriptions") if len(msg) == 0 else await ctx.send(f"{ctx.author} subscribes the following genres: \n{msg}")
        except:
            await ctx.send("something went wrong")
    
