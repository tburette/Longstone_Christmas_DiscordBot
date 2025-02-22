import jokeapi
from jokeapi import Jokes
import asyncio


async def get_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(lang="fr")  # Retrieve a random joke
    return joke


async def jokeToMessage():
    joke = await get_joke()
    message = ""
    if joke["type"] == "single":  # Print the joke
        message = joke["joke"]
    else:
        message = joke["setup"]
        message += "\n||"
        message += joke["delivery"]
        message += "||"
    return message


