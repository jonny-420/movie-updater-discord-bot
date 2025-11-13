from services.getRolesNames import get_roles_names


async def check_user_role(ctx):
    member = ctx.author
    user_roles = get_roles_names(member.roles)
    if "movie watcher" in user_roles:
        return True
    await ctx.send('You don\'t have the necessary role to use this bot')
    return False