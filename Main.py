import asyncio
import discord
import fortnitepy
from fortnitepy import *
from discord.ext import commands
from random import randint
from discord import Interaction
import random
import json

client = commands.Bot(command_prefix=";", intents=discord.Intents.all())
privat = open("./private.json", "r").read()
private = json.loads(privat)
# if ur a new contributor to this bot, add ur discord user id to this list
# for authorization to beta features
contributorsdiscordid = [
    974903535982485504,
    932666698438418522
]

# function to wait for user input
async def wait_for_user_input(ctx) -> str:
    def check(m):
        return m.channel.id == ctx.channel.id and m.author.id == ctx.author.id
    hmmm = await client.wait_for("message", check=check, timeout=60)
    return hmmm

@client.event
async def on_ready():
    print(f"{client.user.name} is logged in as {client.user}.")

@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    exit()

@client.command()
async def say(ctx, a):
    await ctx.send(a)

@client.command()
async def dice(ctx):
    await ctx.send(":game_die: " + str(random.randint(1, 6)))

#i thought this was a fortnite bot
@client.command()
async def math_add(ctx,a,b):
    await ctx.send(float(a) + float(b))

@client.command()
async def math_sub(ctx,a,b):
    await ctx.send(float(a) - float(b))

@client.command()
async def math_times(ctx,a,b):
    await ctx.send(float(a) * float(b))

@client.command()
async def math_divid(ctx,a,b):
    await ctx.send(float(a) / float(b))

@client.command()
async def newsletter(ctx):
    # is this even real
    j = [
        "Waterway search for clues on missing Sydney couple",
        "150 live bugs removed from inside man's nose and sinus cavities",
        "WWII-era bomb discovered in English city safely detonated at sea",
        "Trump wins South Carolina primary, easily beating Haley",
        "Expert warns Russia has 'regrouped', making progress in Ukraine",
        "Trump calls himself a 'proud political dissident' in speech",
        "Body of Russian opposition leader Alexei Navalny now with his mother",
        "Facing backlash over IVF ruling, Alabama lawmakers look for a fix",
        "Zelensky hosts Western leaders as Ukraine marks 2 years since war",
        "Former cop shop transformed into Sydney's first queer history museum",
        "Owl beloved by New York City flies into building and dies",
        "Husband made over $2m by eavesdropping on wife, a BP manager",
        "Blind seal gives birth, nurtures pup at Chicago zoo",
        "Scientists show off 240-million-year-old 'dragon' fossil"
    ]
    finalj = "".join("\n" + item for item in j).removeprefix("\n")
    await ctx.send(finalj)

@client.command()
async def fortnitebot(ctx):
    # alpha comes before beta
    VERSION = "v0.0.1-alpha"
    if ctx.author.id not in contributorsdiscordid:
        await ctx.send("You are not a contributor, so you can't access the beta game.")
    else:
        await ctx.send(f"Alpha Fortnite game ({VERSION})")


client.run(str(private["token"]))