import discord
from discord.ext import tasks, commands
from helper import char
from protected import TOKEN_ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Time to play BREAK!! RPG.")

@bot.slash_command()
async def create(
    message, 
    calling: discord.Option(str, choices=['Factotum', 'Sneak', 'Champion', 'Raider', 'Battle Princess', 'Murder Princess', 'Sage', 'Heretic']),
    species: discord.Option(str, choices=['Human', 'Dimensional Stray', 'Chib', 'Tenebrate', 'Rai-Neko', 'Promethean', 'Gruun', 'Goblin', 'Dwarf', 'Elf', 'Bio-Mechanoid'])
):
    character = char.calling_info(calling)
    character.size = char.species_info(species)
    character.name = message.author.display_name
    character.calling = calling
    character.species = species
    print(character)
    
    
    
# ====    
bot.run(TOKEN_ID)