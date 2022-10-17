# https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

import discord
import sys
from jokes import jokeToMessage

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
discord.ext.commands.DefaultHelpCommand(default_argument_description="")



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

    @bot.command(name='del', brief='Supprimer des messages')
    async def deleteMessages(ctx, number_of_messages: int):
        """
        Description :
            Supprime les n messages précédents

        Argument à saisir après la commande
            - Quantité de messages à supprimer en valeur entière
        """
        try:
            messages = [message async for message in ctx.channel.history(limit=number_of_messages + 1)]
            for message in messages:
                await message.delete()
            message = "Voila, j'ai fais mon travail de nettoyage. Xoxo"
            await ctx.channel.send(message)

        except:
            message = "J'ai un peu de peine à faire mon travail de nettoyage, je m'arrête là... dsl Bro"
            await ctx.channel.send(message)

    @bot.command(name='je_suis', brief="Enregistrer mon nom")
    async def je_suis(ctx):
        """
        Description :
            Permet de faire la relation entre ton nom et ton nom d'utilisateur

        Argument à saisir après la commande
            - Ton nom, s'il y a des espaces, il faut placer ton nom entre " " - Exemple : "José Pinto Silva"
        """
        user = User(str(ctx.author), ctx.message.content.split()[1])
        if exist(user):
            message = f"Merci {user.getName()}, ton nom existe déjà dans ma base de donnée.\n Bisou"
            await ctx.channel.send(message)
        else:
            message = f"Merci {user.getName()}, ton nom a été enregistré dans ma base de donnée.\n" \
                      f"Je t'ai aussi envoyé un message en privé afin de m'assurer que tu reçoives bien mes messages\n" \
                      f"Tes données vont être vendues et on va faire masse pognon\n <3 Bisou"
            global_data.Users.append(user)
            global_data.saveUsers()
            await ctx.channel.send(message)
            private_sent = f"{user.getName()},\nVoici notre première communication !"
            await user.sendPrivateMessage(ctx, private_sent)

    @bot.command(name='en_couple_avec', brief="Définition du conjoint")
    async def en_couple_avec(ctx, partner: str):
        """
        Description :
            Permet de définir son conjoint

        Argument à saisir après la commande
            - le nom du conjoint
        """
        message = getUserByUserName(str(ctx.author)).setPartner(partner)
        await ctx.channel.send(message)

    @bot.command(name='plus_en_couple', brief="Retrait du conjoint")
    async def plus_en_couple_avec(ctx):
        """
        Description :
            Permet de retirer son conjoint

        Argument à saisir après la commande
            - Aucun
        """
        message = getUserByUserName(str(ctx.author)).removePartner()
        await ctx.channel.send(message)


    @bot.command(name='qui_je_suis', brief="Afficher mon nom")
    async def qui_je_suis(ctx):
        """
        Description :
            Permet de retourner le nom qui est associé à toi

        Argument à saisir après la commande
            - Aucun
        """
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

    @bot.command(name='qui_est_qui', brief="Montrer les noms")
    async def qui_est_qui(ctx):
        """
        Description :
            Affiche tous les utilisateurs avec leur nom respectifs

        Argument à saisir après la commande
            - Aucun
        """
        message = "Voici la liste des personnes connues:\n"
        for u in global_data.Users:
            s = f"{u.getUserName()} est {u.getName()}\n"
            message += s
        await ctx.channel.send(message)

    @bot.command(name='oublie_moi', brief="Supprime mon nom")
    async def oublie_moi(ctx):
        """
        Description :
            Supprime ton nom de la base de donnée

            Remarque :  Si tu es inscrit à un Noël, ton nom restera enregistré dans les inscriptions,
                        ton nom ne sera pas disponible pour de futures inscriptions

        Argument à saisir après la commande
            - Aucun
        """
        u = getUserByUserName(str(ctx.author))
        if u is None:
            message = f"Hey {str(ctx.author)} !\nComment veux-tu que je t'oublie je te connais même pas... \nAller zou, loin du bal. bec"
            await ctx.channel.send(message)
            return
        global_data.Users.remove(u)
        global_data.saveUsers()
        message = f"Adieu {u.getUserName()}, connu sous le nom de {u.getName()}.\nPar contre je te rends pas le pognon que je me suis fais avec tes données. Tcho bec"
        await ctx.channel.send(message)

    @bot.command(name='creer_noel', brief="Créer un nouveau noël")
    async def createChristmas(ctx, year: int):
        """
        Description :
            Crée un nouveau noël
            Remarque :  Un noël déjà créé ne peut pas être créé une seconde fois

        Argument à saisir après la commande
            - Année du noël à créer en valeur entière
        """
        message = christmas.newChristmas(year)
        await ctx.channel.send(message)

    @bot.command(name='ouvrir_inscription', brief="Ouvrir des inscriptions")
    async def openRegistration(ctx, year: int):
        """
           Description :
               Ouvre les inscriptions

           Argument à saisir après la commande
               - Année du noël dont on veut ouvrir les inscriptions, en valeur entière
           """
        message = christmas.openRegistration(year)
        await ctx.channel.send(message)

    @bot.command(name='fermer_inscription', brief="Fermer des inscriptions")
    async def openRegistration(ctx, year: int):
        """
           Description :
               Ferme les inscriptions

           Argument à saisir après la commande
               - Année du noël dont on veut fermer les inscriptions, en valeur entière
           """
        message = christmas.closeRegistration(year)
        await ctx.channel.send(message)

    @bot.command(name='je_participe_a_noel', brief="Inscrire sa participation")
    async def registreChristmas(ctx, year: int):
        """
           Description :
               Inscrit ta participation

           Argument à saisir après la commande
               - Année du noël dont on veut fermer les inscriptions, en valeur entière
           """
        message = christmas.registre(getUserByUserName(str(ctx.author)), year)
        await ctx.channel.send(message)

    @bot.command(name='noel_info', brief="Info du noël", description="Affiche les informations du noël de l'année saisie après la commande")
    async def christmasInfo(ctx, year: int):
        """
           Description :
               Affiche les informations de noël

           Argument à saisir après la commande
               - Année du noël dont on veut avoir des informations, en valeur entière
        """
        message = ""
        if christmas.indexOfChristmas(year) == -1:
            message = f"Noël {year} n'existe pas"
        else:
            message = global_data.Christmas[christmas.indexOfChristmas(year)].info()
        await ctx.channel.send(message)

    @bot.command(name='tirage', brief="Tirage au sort pour noel")
    async def tirage(ctx, year: int):
        """
                  Description :
                      Fait le tirage au sort pour les cadeaux de noël

                  Argument à saisir après la commande
                      - Année du noël dont on veut faire le tirage au sort, en valeur entière
               """
        message = ""
        index = christmas.indexOfChristmas(year)
        if index != -1:
            pair = global_data.Christmas[index].getPairs()
            message = "Voici les pairs:\n--------------\n"
            for p in pair:
                message += f"{p}\n"
        else:
            message = f"Noël {year} n'existe pas"
        await ctx.channel.send(message)


    @bot.command(name='pere_castor', brief="Raconte une histoire")
    async def joke(ctx):
        """
           Description :
               Affiche une joke monstre drôle

           Argument à saisir après la commande
               - Aucun
        """
        message = await jokeToMessage()
        await ctx.channel.send(message)

    bot.run("MTAyOTgzNDI0Njk1MDQ5NDM3OQ.GpLGpy._O7YR6oMtVg4fbY6p8xUKY6QUSMk_u8ZUvX6gI")
