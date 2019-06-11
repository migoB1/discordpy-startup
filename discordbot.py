from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))




@bot.command()
async def ping(ctx):
    aaa=random.randrange(len(goroku_a))
    await ctx.send(goroku_a[aaa])


bot.run(token)
