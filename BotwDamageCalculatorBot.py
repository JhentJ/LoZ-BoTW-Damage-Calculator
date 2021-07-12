import discord
from discord.ext import commands
import random
import BACKUPFullWeaponList

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['Sword'])
async def _8ball(ctx, *, question):
     BACKUPFullWeaponList.AllWeapons
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run("ODM5MzE2MzQyNzgzMzQ0NjUx.YJH4QQ.bOn3Qfsn5Ja3OQtZzHBI4iwpEpg")