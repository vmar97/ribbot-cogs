import discord
import requests
import json
from redbot.core import commands
from random import choice

class Nookipedia(commands.Cog):
        """Grab information from Nookipedia"""

        def __init__(self, bot):
                self.bot = bot

        @commands.command(pass_context=True)
        async def villager(self, ctx, villager, *args):
                apikey = 'INSERT_API_HERE'
                for arg in args:
                        villager = villager + " " + arg
                if (villager.lower() == "renee"):
                        villager = 'Renée'
                elif (villager.lower() == "etoile"):
                        villager = 'Étoile'
                if villager.lower() == "random":
                        apilink = requests.get('https://api.nookipedia.com/villagers?nhdetails=true&api_key=' + apikey)
                        nookapi = choice(apilink.json())
                        name = nookapi["name"]
                        url = nookapi["url"]
                        titlecolor = nookapi["title_color"]
                        image = nookapi["image_url"]
                        species = nookapi["species"]
                        personality = nookapi["personality"]
                        gender = nookapi["gender"]
                        birthdaymonth = nookapi["birthday_month"]
                        birthday = nookapi["birthday_day"]
                        sign = nookapi["sign"]
                        quote = nookapi["quote"]
                        phrase = nookapi["phrase"]
                        clothing = nookapi["clothing"]
                        nhdetails = nookapi["nh_details"]
                        if bool(nhdetails) == True:
                            photo = nookapi["nh_details"]["photo_url"]
                            variation = nookapi["nh_details"]["clothing_variation"]
                else:
                        if villager.lower() == 'carmen mouse':
                            apilink = requests.get('https://api.nookipedia.com/villagers?name=Carmen&species=Mouse&nhdetails=true&api_key=' + apikey)
                        elif villager.lower() == 'lulu':
                            apilink = requests.get('https://api.nookipedia.com/villagers?name=Lulu&species=Hippo&nhdetails=true&api_key=' + apikey)
                        elif villager.lower() == 'lulu islander':
                            apilink = requests.get('https://api.nookipedia.com/villagers?name=Lulu&species=Anteater&nhdetails=true&api_key=' + apikey)
                        elif villager.lower() == 'petunia rhino' or villager.lower() == 'petunia rhinoceros':
                            apilink = requests.get('https://api.nookipedia.com/villagers?name=Petunia&species=Rhinoceros&nhdetails=true&api_key=' + apikey)
                        else:
                            apilink = requests.get('https://api.nookipedia.com/villagers?name=' + villager + '&nhdetails=true&api_key=' + apikey)
                        nookapi = apilink.json()
                        name = nookapi[0]["name"]
                        url = nookapi[0]["url"]
                        titlecolor = nookapi[0]["title_color"]
                        image = nookapi[0]["image_url"]
                        species = nookapi[0]["species"]
                        personality = nookapi[0]["personality"]
                        gender = nookapi[0]["gender"]
                        birthdaymonth = nookapi[0]["birthday_month"]
                        birthday = nookapi[0]["birthday_day"]
                        sign = nookapi[0]["sign"]
                        quote = nookapi[0]["quote"]
                        phrase = nookapi[0]["phrase"]
                        clothing = nookapi[0]["clothing"]
                        nhdetails = nookapi[0]["nh_details"]
                        if bool(nhdetails) == True:
                            photo = nookapi[0]["nh_details"]["photo_url"]
                            variation = nookapi[0]["nh_details"]["clothing_variation"]

                if bool(nookapi) == False:
                        data = discord.Embed()
                        data.add_field(name="Error", value="Villager does not exist!", inline=False)
                else:
                        if bool(titlecolor) == True:
                                villagercol = int(titlecolor, 16)
                        else:
                                villagercol = int('67ac42', 16)
                        data = discord.Embed(title="Villager info", colour=villagercol, description=quote)
                        data.set_thumbnail(url=image)
                        if bool(nhdetails) == True:
                                data.set_author(name=name, url=url, icon_url=photo)
                        else:
                                data.set_author(name=name, url=url)
                        data.add_field(name="Species", value=species, inline=True)
                        data.add_field(name="Personality", value=personality, inline=True)
                        data.add_field(name="Gender", value=gender, inline=True)
                        if bool(birthdaymonth) == True:
                                data.add_field(name="Birthday", value=birthdaymonth + ' ' + str(birthday), inline=True)
                        else:
                                data.add_field(name="Birthday", value="Unknown", inline=True)
                        data.add_field(name="Sign", value=sign, inline=True)
                        data.add_field(name="Catchphrase", value=phrase, inline=True)
                        if bool(nhdetails) == True:
                                clothingtolink = clothing.replace(" ", "_")
                                clothinglink = "https://nookipedia.com/wiki/Item:" + clothingtolink + "_%28New_Horizons%29"
                                if bool(variation) == True:
                                        data.add_field(name="Clothing", value="[" + clothing + "](" + clothinglink + ") (" + variation + ")", inline=True)
                                else:
                                        data.add_field(name="Clothing", value="[" + clothing + "](" + clothinglink + ")", inline=True)
                        else:
                                data.add_field(name="Clothing", value=clothing, inline=True)
                        data.add_field(name="More Info", value="[Learn more on Nookipedia](" + url + ")", inline=True)
                        if villager.lower() == 'carmen':
                            data.set_footer(text="Powered by Nookipedia -- For the mouse villager, type !villager Carmen Mouse", icon_url='https://nookipedia.com/favicon.ico')
                        elif villager.lower() == 'carmen mouse':
                            data.set_footer(text="Powered by Nookipedia -- For the rabbit villager, type !villager Carmen", icon_url='https://nookipedia.com/favicon.ico')
                        elif villager.lower() == 'lulu':
                            data.set_footer(text="Powered by Nookipedia -- For the anteater villager, type !villager Lulu Islander", icon_url='https://nookipedia.com/favicon.ico')
                        elif villager.lower() == 'lulu islander':
                            data.set_footer(text="Powered by Nookipedia -- For the hippo villager, type !villager Lulu", icon_url='https://nookipedia.com/favicon.ico')
                        elif villager.lower() == 'petunia':
                            data.set_footer(text="Powered by Nookipedia -- For the rhinocros villager, type !villager Petunia rhinoceros", icon_url='https://nookipedia.com/favicon.ico')
                        elif villager.lower() == 'petunia rhino' or villager.lower() == 'petunia rhinoceros':
                            data.set_footer(text="Powered by Nookipedia -- For the cow villager, type !villager Petunia", icon_url='https://nookipedia.com/favicon.ico')
                        else:
                            data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)

        @commands.command(pass_context=True)
        async def fish(self, ctx, fish, *args):
                for arg in args:
                        fish = fish + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/fish/' + fish + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('66ccff', 16)
                data = discord.Embed(title="Fish info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.add_field(name="Sell (C.J.)", value=nookapi["sell_cj"], inline=True)
                data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi["url"] + ")", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)

        @commands.command(pass_context=True)
        async def bug(self, ctx, bug, *args):
                for arg in args:
                        bug = bug + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/bugs/' + bug + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('caed78', 16)
                data = discord.Embed(title="Bug info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.add_field(name="Sell (Flick)", value=nookapi["sell_flick"], inline=True)
                data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi["url"] + ")", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)

        @commands.command(pass_context=True)
        async def seacrit(self, ctx, seacrit, *args):
                for arg in args:
                        seacrit = seacrit + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/sea/' + seacrit + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('66a6ff', 16)
                data = discord.Embed(title="Sea creature info", colour=coloring, description=nookapi["catchphrases"][0])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Months (NH)", value=nookapi["north"]["months"], inline=True)
                data.add_field(name="Months (SH)", value=nookapi["south"]["months"], inline=True)
                data.add_field(name="Times", value=nookapi["north"]["availability_array"][0]["time"], inline=True)
                data.add_field(name="Sell", value=nookapi["sell_nook"], inline=True)
                data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi["url"] + ")", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)

        @commands.command(pass_context=True)
        async def art(self, ctx, art, *args):
                for arg in args:
                        art = art + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/art/' + art + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('e1a884', 16)
                data = discord.Embed(title="Art info", colour=coloring, description=nookapi["description"])
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])
                data.add_field(name="Real-world name", value=nookapi["art_name"], inline=True)
                data.add_field(name="Author", value=nookapi["author"], inline=True)
                data.add_field(name="Year", value=nookapi["year"], inline=True)
                data.add_field(name="Art style", value=nookapi["art_style"], inline=True)
                if nookapi["has_fake"] == True:
                        data.add_field(name="Can be fake?", value="Yes", inline=True)
                else:
                        data.add_field(name="Can be fake?", value="No", inline=True)
                data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi["url"] + ")", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)

        @commands.command(pass_context=True)
        async def recipe(self, ctx, recipe, *args):
                for arg in args:
                        recipe = recipe + " " + arg
                apikey = 'INSERT_API_HERE'
                apilink = requests.get('https://api.nookipedia.com/nh/recipes/' + recipe + '?api_key=' + apikey)
                nookapi = apilink.json()
                coloring = int('ffc966', 16)
                data = discord.Embed(title="Recipe info", colour=coloring)
                data.set_thumbnail(url=nookapi["image_url"])
                data.set_author(name=nookapi["name"], url=nookapi["url"])

                availall = ""
                for availability in range (len(nookapi["availability"])):
                	if nookapi["availability"][availability]["note"]:
                		avail = nookapi["availability"][availability]["from"] + " (" + nookapi["availability"][availability]["note"] + ")"
                	else:
                		avail = nookapi["availability"][availability]["from"]
                	if availability < int(len(nookapi["materials"])) - 1:
                		availall += avail + '\n'
                	else:
                		availall += avail

                matall = ""
                for material in range (len(nookapi["materials"])):
                	mat = str(nookapi["materials"][material]["count"]) + "× " + nookapi["materials"][material]["name"]
                	if material < int(len(nookapi["materials"])) - 1:
                		matall += mat + '\n'
                	else:
                		matall += mat

                data.add_field(name="Obtained via", value=availall, inline=False)
                data.add_field(name="Recipes to unlock", value=nookapi["recipes_to_unlock"], inline=True)
                data.add_field(name="Materials", value=matall, inline=True)
                data.add_field(name="More Info", value="[Learn more on Nookipedia](" + nookapi["url"] + ")", inline=True)
                data.set_footer(text='Powered by Nookipedia', icon_url='https://nookipedia.com/favicon.ico')
                await ctx.send(embed=data)
