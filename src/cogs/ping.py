import discord
from discord.ext import commands

client = discord.Client()


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Yamashiro is online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! | Latency: {round(client.latency * 1000)}ms") #bugged

def setup(client):
    client.add_cog(Ping(client))
