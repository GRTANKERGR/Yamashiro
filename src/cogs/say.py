import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = Bot(command_prefix='$')

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.command(pass_context = True)
    async def say(self, ctx, *message):
        await ctx.message.delete_message()
        await ctx.send(message)

def setup(client):
    client.add_cog(Say(client))