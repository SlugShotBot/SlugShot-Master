import discord
import random, math
import autolist

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hi there, {}'.format(message.author.mention))


#Token should be added here from Developer Portal
bot.run('Token')
