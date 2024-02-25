import asyncio
import discord
import fortnitepy
from fortnitepy import *
from discord.ext import commands
from random import randint
from discord import Interaction
import random

client = commands.Bot(command_prefix=";", intents=discord.Intents.all())

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
    j1 = "Waterway search for clues on missing Sydney couple"
    j2 = "150 live bugs removed from inside man's nose and sinus cavities"
    j3 = "WWII-era bomb discovered in English city safely detonated at sea"
    j4 = "Trump wins South Carolina primary, easily beating Haley"
    j5 = "Expert warns Russia has 'regrouped', making progress in Ukraine"
    j6 = "Trump calls himself a 'proud political dissident' in speech"
    j7 = "Body of Russian opposition leader Alexei Navalny now with his mother"
    j8 = "Facing backlash over IVF ruling, Alabama lawmakers look for a fix"
    j9 = "Zelensky hosts Western leaders as Ukraine marks 2 years since war"
    j10 = "Former cop shop transformed into Sydney's first queer history museum"
    j11 = "Owl beloved by New York City flies into building and dies"
    j12 = "Husband made over $2m by eavesdropping on wife, a BP manager"
    j13 = "Blind seal gives birth, nurtures pup at Chicago zoo"
    j14 = "Scientists show off 240-million-year-old 'dragon' fossil"
    await ctx.ssend(j1)
    await ctx.send(j2)
    await ctx.send(j3)
    await ctx.send(j4)
    await ctx.send(j5)
    await ctx.send(j6)
    await ctx.send(j7)
    await ctx.send(j8)
    await ctx.send(j9)
    await ctx.send(j10)
    await ctx.send(j11)
    await ctx.send(j12)
    await ctx.send(j13)
    await ctx.send(j14)




@client.command()
async def fortnitebot(ctx):
    await ctx.send("Beta Fortnite game")














client.run("MTIxMDg1MDg3NTE5MTQ1OTg0MQ.GCziiZ.kSwonaKqTOU5b2ovcW0nNr40rifRNVgcE9QrVY")