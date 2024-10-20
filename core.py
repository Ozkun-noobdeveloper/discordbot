import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"已登入為 {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 從 Render 的環境變數取得 Token
bot.run(os.getenv("DISCORD_TOKEN"))