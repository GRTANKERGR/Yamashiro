#!/usr/bin/env python
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        client.load_extension(f"cogs.music.player")

client.run("NzE5OTA2MzAyMDM3NTkwMTM4.XudMZg.PuTn4NXCP3HDQy8Ee4S1nuVZr7k")