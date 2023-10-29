from discord.ext import commands
import discord
from discord import app_commands
import os
import minarai.cogs as cogs

client = commands.Bot(intents=discord.Intents.all(), command_prefix="m!", application_id="1168023091847368714")

@client.event
async def on_ready():
    await cogs.setup(client=client)
    print("[STATUS]: Online")

client.run(os.environ["DISCORD_TOKEN"])
