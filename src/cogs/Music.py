import re

import discord
import wavelink
from discord.ext import commands

url_rx = re.compile(r'https?://(?:www\.)?.+')


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        await self.bot.wavelink.initiate_node(host='127.0.0.1',
                                              port=2333,
                                              rest_uri='http://127.0.0.1:2333',
                                              password='youshallnotpass',
                                              identifier='TEST',
                                              region='us_central')

    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                await ctx.send("No channel to join. Please either specify a valid channel or join one.")
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await player.connect(channel.id)
        await ctx.send(f'Connected to **`{channel.name}`**')

    @commands.command(name="leave")
    async def leave(self, ctx, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                await ctx.send("I'm not in a voice channel!")
                raise discord.DiscordException("User executed leave command without the yama ever joining in.. :pepega:")

            player = self.bot.wavelink.get_player(ctx.guild.id)
            await player.disconnect()
            await ctx.send(f"I've left **{channel.name}**")

    @commands.command()
    async def play(self, ctx, *, query: str):
        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

        if not tracks:
            return await ctx.send('Could not find any songs with that query.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        await ctx.send(f'Added {str(tracks[0])} to the queue.')
        await player.play(tracks[0])

    @commands.command(name="stop")
    async def stop(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)
        
        if not player.is_connected:
            await ctx.send("Please join a voice channel first before executing this command!")
        await player.stop()

    @commands.command(name="volume")
    async def set_volume(self, ctx, volume):
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            if volume > 1000:
                await ctx.send("Set the volume between 0 and 200")
            elif volume < 1000:
                await player.set_volume(volume)
        except:
            await ctx.send("I couldn't change the volume.. for some reason :/")
            raise discord.DiscordException("Failed to change volume")


def setup(bot):
    bot.add_cog(Music(bot))