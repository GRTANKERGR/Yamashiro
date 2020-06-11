import discord
client = discord.Client()


@client.event
async def on_ready():
    print("Yamashiro is ready!")


client.run("NzE5OTA2MzAyMDM3NTkwMTM4.XuI3Gg.1HkD1dm9tBhcDpwdPv92bjZqqho")