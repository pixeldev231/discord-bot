from random import randint
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    syncs = await bot.tree.sync()
    print(f"{len(syncs)} commandos")
    print("bot inicializado com sucesso")

@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f"Olá {interact.user.mention}!")
    

@bot.tree.command()
async def say(interact:discord.Interaction, texto:str):
    await interact.response.send_message(texto)

@bot.tree.command()
async def somar(interact:discord.Interaction, num1:int, num2:int):
    numero = num1 + num2
    await interact.response.send_message(f"A Soma Entre Os Numeros {num1} e {num2} é {numero}")
    
@bot.tree.command()
async def multiplicar(interact:discord.Interaction, num1:int, num2:int):
    numero = num1 * num2
    await interact.response.send_message(f"A multiplicação Entre Os Numeros {num1} e {num2} é {numero}")
    
@bot.tree.command()
async def subtrair(interact:discord.Interaction, num1:int, num2:int):
    numero = num1 - num2
    await interact.response.send_message(f"A subtração Entre Os Numeros {num1} e {num2} é {numero}")
    
@bot.tree.command()
async def dividir(interact:discord.Interaction, num1:int, num2:int):
    numero = float(num1 / num2)
    await interact.response.send_message(f"A divisão Entre Os Numeros {num1} e {num2} é {numero}")
    
@bot.tree.command()
async def random(interact:discord.Interaction):
    numero = randint(1, 1000)
    await interact.response.send_message(f"aqui esta {numero}")
    
@bot.tree.command()
async def help(interact:discord.Interaction):
    comandos = await bot.tree.sync()
    await interact.response.send_message(f"aqui estão meus comandos {comandos}")

bot.run("MTM2ODA3OTQ3NjQ0OTA4NzUzOA.GoSbXR.RkDfY1T3j3rO4P5GMFwvXPDiwsnTQ1z9Zm1K9I")

