# https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

import discord
import sys

from discord.ext import commands
import global_data
from help import help
from global_data import Users
from user import User, exist, getUserByUserName
import christmas
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

    @bot.command(name='del', brief='Supprime les n messages de la valeur saisie après la commande')
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

    @bot.command(name='je_suis', brief="Prend connaissance du nom de l'utilisateur saisi après la commande")
    async def je_suis(ctx):
        user = User(str(ctx.author), ctx.message.content.split()[1])
        if (exist(user)):
            message = f"Merci {user.getName()}, ton nom existe déjà dans ma base de donnée.\n Bisou"
            await ctx.channel.send(message)
        else:
            message = f"Merci {user.getName()}, ton nom a été enregistré dans ma base de donnée. Tes données vont être vendues et on va faire masse pognon\n <3 Bisou"
            global_data.Users.append(user)
            global_data.saveUsers()
            await ctx.channel.send(message)

    @bot.command(name='qui_je_suis', brief="Affiche le nom enregistré")
    async def qui_je_suis(ctx):
        user = None
        for u in global_data.Users:
            if u.getUserName() == str(ctx.author):
                user = u
                break

        if user is None:
            message = f"{str(ctx.author)}, \nÀ mes yeux tu n'es rien qu'un utilisateur de discord... je ne te connais pas.\nSi tu veux que j'apprenne ton nom, tape $je_suis suivi de ton nom\nTcho bonne bec!"
            await ctx.channel.send(message)
            return
        message = f"Tcho {user.getUserName()}!\n Tu es connu sous le nom de {user.getName()}.\nC'est pas très joli mais ça te va bien.\nSalut Tcho bec"
        await ctx.channel.send(message)

    @bot.command(name='qui_est_qui', brief="Montre les noms et les noms d'utilisateurs")
    async def qui_est_qui(ctx):
        message = "Voici la liste des personnes connues:\n"
        for u in global_data.Users:
            s = f"{u.getUserName()} est {u.getName()}"
            message += s
        await ctx.channel.send(message)

    @bot.command(name='oublie_moi', brief="Supprime le nom de la base de donnée")
    async def oublie_moi(ctx):
        u = getUserByUserName(str(ctx.author))
        if u is None:
            message = f"Hey {str(ctx.author)} !\nComment veux-tu que je t'oublie je te connais même pas... \nAller zou, loin du bal. bec"
            await ctx.channel.send(message)
            return
        global_data.Users.remove(u)
        global_data.saveUsers()
        message = f"Adieu {u.getUserName()}, connu sous le nom de {u.getName()}.\nPar contre je te rends pas le pognon que je me suis fais avec tes données. Tcho bec"
        await ctx.channel.send(message)

    @bot.command(name='creer_noel', brief="Crée un nouveau noël pour l'année saisie après la commande")
    async def createChristmas(ctx, year: int):
        message = christmas.newChristmas(year)
        await ctx.channel.send(message)

    @bot.command(name='ouvrir_inscription', brief="Ouvre les inscriptions du noël de l'année saisie après la commande")
    async def openRegistration(ctx, year: int):
        message = christmas.openRegistration(year)
        await ctx.channel.send(message)

    @bot.command(name='fermer_inscription', brief="Ferme les inscriptions du noël de l'année saisie après la commande")
    async def openRegistration(ctx, year: int):
        message = christmas.closeRegistration(year)
        await ctx.channel.send(message)

    @bot.command(name='je_participe_a_noel', brief="Inscrit ta participation au noël de l'année saisie après la commande")
    async def registreChristmas(ctx, year: int):
        message = christmas.registre(getUserByUserName(str(ctx.author)), year)
        await ctx.channel.send(message)

    @bot.command(name='noel_info', brief="Affiche les info du noël de l'année saisie après la commande")
    async def registreChristmas(ctx, year: int):
        message = ""
        if christmas.indexOfChristmas(year) == -1:
            message = f"Noël {year} n'existe pas"
        else:
            message = global_data.Christmas[christmas.indexOfChristmas(year)].info()
        await ctx.channel.send(message)

    bot.run("MTAyOTgzNDI0Njk1MDQ5NDM3OQ.GpLGpy._O7YR6oMtVg4fbY6p8xUKY6QUSMk_u8ZUvX6gI")
