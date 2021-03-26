import discord
from discord.ext import commands
from lxml import html
import requests
import re

class villagerLookup:
        """Grab villager information from Nookipedia"""
		

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager):
                data = discord.Embed(title=villager, url=url, color=title_color, description=quote)
                api-key = 'INSERT_API_HERE'
                page = requests.get('https://api.nookipedia.com/villagers?name=' + villager + '&api_key=' + api-key)
                attributes = ["url", "title_color", "image_url", "species", "personality", "gender", "birthday_month", "birthday_day", "sign", "quote", "phrase"]
                if page.status_code == 404:
                        data.add_field(name="Error", value="Villager does not exist!")
                else:
                        data.set_thumbnail(url=image_url)
                        embed.add_field(name="Species", value=species, inline=True)
						embed.add_field(name="personality", value=personality, inline=True)
						embed.add_field(name="gender", value=gender, inline=True)
						embed.add_field(name="Birthday", value=birthday_month + ' ' + str(birthday_day), inline=True)
						embed.add_field(name="Sign", value=sign, inline=True)
						embed.add_field(name="Catchphrase", value=phrase, inline=True)
						embed.add_field(name="More info", value='Learn more on Nookipedia', url=url, inline=True)

def setup(bot):
	bot.add_cog(villagerLookup(bot))
