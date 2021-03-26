from redbot.core import commands
import discord
import requests
import json

class Villager(commands.Cog):
        """Grab villager information from Nookipedia"""

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager):
                if villager == "Renee" or villager == "renee":
                        villager = 'Renée'
                elif villager == "Etoile" or villager == "etoile":
                        villager = 'Étoile'
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/villagers?name=' + villager + '&nhdetails=true&api_key=' + apikey)
                nookapi = apilink.json()
                villagercol = int(nookapi[0]['title_color'], 16)
                data = discord.Embed(title=villager, url=nookapi[0]["url"], colour=villagercol, description=nookapi[0]["quote"])
                if nookapi == "[]":
                        data.add_field(name="Error", value="Villager does not exist!")
                else:
                        data.set_image(url=nookapi[0]["image_url"])
                        if bool(nookapi[0]["nh_details"]["photo_url"]) == True:
                         data.set_thumbnail(url=nookapi[0]["nh_details"]["photo_url"])

                        data.add_field(name="Species", value=nookapi[0]["species"], inline=True)
                        data.add_field(name="Personality", value=nookapi[0]["personality"], inline=True)
                        data.add_field(name="Gender", value=nookapi[0]["gender"], inline=True)
                        data.add_field(name="Birthday", value=nookapi[0]["birthday_month"] + ' ' + str(nookapi[0]["birthday_day"]), inline=True)
                        data.add_field(name="Sign", value=nookapi[0]["sign"], inline=True)
                        data.add_field(name="Catchphrase", value=nookapi[0]["phrase"], inline=True)
                        data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
