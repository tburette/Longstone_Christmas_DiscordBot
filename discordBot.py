# https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

import discord
import sys

from discord.ext import commands
import global_data
from help import help
from global_data import Users
from user import User, exist

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


def run():
    @bot.event
    async def on_ready():
        global_data.load_data()
        print("The bot is ready")

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        message = await message.channel.fetch_message(message.id)
        if message is None:
            return  # gets the message with id
        print(message.content)

    @bot.command(name='commandes')
    async def printHelp(ctx):
        message = f"```\n{help}\n```"
        await ctx.channel.send(message)

    @bot.command(name='del')
    async def deleteMessages(ctx, number_of_messages: int):
        try:
            messages = [message async for message in ctx.channel.history(limit=number_of_messages + 1)]
            for message in messages:
                await message.delete()
            message = "Voila, j'ai fais mon travail de nettoyage. Xoxo"
            await ctx.channel.send(message)

        except:
            message = "J'ai un peu de peine à faire mon travail de nettoyage, je m'arrête là... dsl Bro"
            await ctx.channel.send(message)

    @bot.command(name='je_suis')
    async def je_suis(ctx):
        user = User(str(ctx.author), ctx.message.content.split()[1])
        if (exist(user)):
            message = f"Merci {user.getName()}, ton nom existe déjà dans ma base de donnée.\n Bisou"
            await ctx.channel.send(message)
        else:
            message = f"Merci {user.getName()}, ton nom a été enregistré dans ma base de donnée. Tes données vont être vendues et on va faire masse pognon\n <3 Bisou"
            Users.append(user)
            global_data.saveUsers()
            await ctx.channel.send(message)

    @bot.command(name='oublie_moi')
    async def oublie_moi(ctx):
        user = None
        for u in global_data.Users:
            if u.getUserName() == str(ctx.author):
                user = u
                break

        if user is None:
            message = f"Hey {user.getUserName()} !\nComment veux-tu que je t'oublie je te connais même pas... \nAller zou, loin du bal. bec"
            await ctx.channel.send(message)
            return
        global_data.Users.remove(user)
        global_data.saveUsers()
        message = f"Adieu {user.getUserName()}, connu sous le nom de {user.getName()}.\nPar contre je te rends pas le pognon que je me suis fais avec tes données. Tcho bec"
        await ctx.channel.send(message)


    bot.run("MTAyOTgzNDI0Njk1MDQ5NDM3OQ.GpLGpy._O7YR6oMtVg4fbY6p8xUKY6QUSMk_u8ZUvX6gI")
