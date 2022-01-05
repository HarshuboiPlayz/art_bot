# import server
import server
import discord
import random
import os

list_of_art = ["Dragon", "Bird", "Shrek", "Discord Logo", "Ghost", "Doll", "Custom Creature/Monster", "Animal Hybrid", "Vampire (with clothes)", "Basic Human (with clothes)", "Zombie (with clothes)", "Werewolf (with clothes)", "Plant", "Flower", "Rose", "Bat", "Chinchilla", "Fox", "Cat", "Dog", "Phoenix", "Unicorn", "Pegasus", "Unisus", "Gargoyle", "Prince/Pricess (with clothes)", "Queen/King (with clothes)", "Merman/Mermaid (with clothes)", "Witch/Wizard (with clothes)", "Paranormal Investigator (with clothes)", "Detective", "Assasin"]

pallet = ["Red", "Blue", "Green", "Brown", "Yellow", "Magenta", "Pink", "Purple", "White", "Black", "Pastel Red", "Pastel Blue", "Pastel Green", "Pastel Brown", "Pastel Yellow", "Pastel Magenta", "Pastel Pink", "Pastel Purple", "Pastel White"]

personality = ["Happy", "Angry", "Bully", "Loving", "Kind", "Fighter"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!art'):
        await message.channel.send("The Random Thing You Have To Draw Is" + " " + random.choice(list_of_art) + " " + "With The Color's of " + random.choice(pallet) + ", " + random.choice(pallet) + ", " + random.choice(pallet) + " " + "And With The Personality Of " + random.choice(personality))

    if message.content.startswith('!invite'):
        await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=863298281396633650&permissions=534789880640&scope=bot")

    if message.content.startswith('!help'):
        await message.channel.send("""```My Commands:
				!help - Shows This
				!art - Sends A Random Art Suggestion
				!invite - Sends The Invite Link```""")


TOKEN = os.getenv("TOKEN")
# host index.html
server.super_run()
client.run(TOKEN)