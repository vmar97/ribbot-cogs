from .nookipedia import Nookipedia

def setup(bot):
    cog = Nookipedia(bot)
    bot.add_cog(cog)
