import discord
from discord.ext import commands

client = discord.Client()

class Reboot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reboot(self, ctx):
        try:
            await client.logout()
            await client.run("NzE5OTA2MzAyMDM3NTkwMTM4.XudMZg.PuTn4NXCP3HDQy8Ee4S1nuVZr7k")
        except Exception:
            print("Error: Couldn't reboot\n")

def setup(client):
    client.add_cog(Reboot(client))