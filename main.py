#https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True



bot = commands.Bot(command_prefix='$', intents=intents)

mapUserName = []

@bot.event
async def on_ready():
    print("The bot is ready")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    message = await message.channel.fetch_message(message.id)
    if message is None:
        return  # gets the message with id
    print(message.content)


@bot.command(name='del')
async def deleteMessages(ctx, number_of_messages: int):
    messages = [message async for message in ctx.channel.history(limit=number_of_messages + 1)]

    for message in messages:
        await message.delete()


@bot.command(name='name')
async def map_name_with_username(ctx):
    author = ctx.author
    name = ctx.message.content.split()[1]
    mapUserName.append((author, name))
    print(f"{author} est {name}")




bot.run("MTAyOTgzNDI0Njk1MDQ5NDM3OQ.GpLGpy._O7YR6oMtVg4fbY6p8xUKY6QUSMk_u8ZUvX6gI")

