import discord

class YamashiroClient(discord.Client):

    async def on_ready(self):
        print("Yamashiro is ready!")

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = YamashiroClient()
client.run("NzE5OTA2MzAyMDM3NTkwMTM4.XuI3Gg.1HkD1dm9tBhcDpwdPv92bjZqqho")