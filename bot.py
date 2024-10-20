import os
import discord
from discord.ext import commands

# 設置 intents
intents = discord.Intents.default()
intents.message_content = True  # 啟用訊息內容意圖

# 初始化 Bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 使用環境變數中的 Token 啟動 Bot
bot.run(os.getenv('DISCORD_TOKEN'))
