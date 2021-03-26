import discord
from discord.ext import commands
from lxml import html
import requests
import json

class villagerLookup:
        """Grab villager information from Nookipedia"""
		

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager):
                apilink = requests.get('https://api.nookipedia.com/villagers?name=' + villager + '&api_key=' + api-key)
                api-key = 'INSERT_API_HERE'
                data = discord.Embed(title=villager, url=nookapi["url"], color=nookapi["title_color"], description=nookapi["quote"])
                nookapi = json.loads(apilink.text)
                if nookapi == "[]":
                        data.add_field(name="Error", value="Villager does not exist!")
                else:
                        data.set_thumbnail(url=image_url)
                        data.add_field(name="Species", value=nookapi["species"], inline=True)
                        data.add_field(name="Personality", value=nookapi["personality"], inline=True)
                        data.add_field(name="Gender", value=nookapi["gender"], inline=True)
                        data.add_field(name="Birthday", value=nookapi["birthday_month"] + ' ' + str(nookapi["birthday_day"]), inline=True)
                        data.add_field(name="Sign", value=nookapi["sign"], inline=True)
                        data.add_field(name="Catchphrase", value=nookapi["phrase"], inline=True)
                        data.add_field(name="More info", value='Learn more on Nookipedia', url=nookapi["url"], inline=True)

def setup(bot):
	bot.add_cog(villagerLookup(bot))
