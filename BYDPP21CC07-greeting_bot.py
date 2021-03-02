'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #07 (BYDPP21CC07)
26 Feb 2021, 8pm GMT
Host: @Λcє
Coach: @alexandros
 
Task
Create a basic Discord Bot that replies to a user greeting
in a specific server and channel.

Installation Required
> discord package

Python Code
As below, being non-optimised, as in the call with minor edits.
'''

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="--")

@bot.event
async def on_ready():
    print(bot.user, 'is ready.')

@bot.event
async def on_message(msg):
    # if the bot is in a specific server
    if msg.guild.id == 664967447534764033:
        # if the message sender is not any bot
        # if not msg.author.bot:
        # if the message sender is not the bot itself
        if msg.author != bot.user:
            await msg.channel.send(f'you sent {msg.content}')
        # if the message is 'hi'
        if msg.content == 'hi':
            # select a channel by id
            channel = bot.get_channel(666564284880388097)
            # send a 'Hello' reply
            return await channel.send('Hello')

bot.run('<YOUR DISCORD BOT TOKEN. Create a bot at https://discord.com/developers/applications>')
