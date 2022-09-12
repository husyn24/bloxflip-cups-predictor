from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print('ready')

@bot.command()
async def cups(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        prediction = random.randint(1,2)
        if prediction == 1:
            embed_color= 0xFF0036
            text = 'Red Cup'
            prediction = ":red_square:"
        elif prediction == 2:
            embed_color= 0x3498DB
            text = 'Blue Cup'
            prediction = ":blue_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Cups Predictor", value=text + "\n" + prediction)
        em.set_footer(text="Made by husyn")
        await ctx.send(embed=em)
    else:
        await ctx.send("Invalid round id")





bot.run('')
