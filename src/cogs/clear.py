import discord
from discord.ext import commands

client = discord.Client()

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, message_limit=1000):
        if message_limit > 1000:
            await ctx.send("I can't delete that many messages! Choose a number between 1 to 1000")
        elif message_limit < 1000:
            await ctx.channel.purge(limit=message_limit)

def setup(client):
    client.add_cog(Clear(client))
