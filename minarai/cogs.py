from discord.ext import commands
from discord import app_commands, ui
import discord
from .API.grammar import Grammar
from .interaction.grammar import GrammarUI
from .interaction.wolfram import wolframInitChoice

class Cogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("[COGS] Listener initiated")
    
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx) -> None:
        await ctx.send("Syncing...")
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(fmt)} commands")
    
    @app_commands.command(name="grammar", description="Proofreads your text to find any grammatical errors.")
    async def grammar(self, interaction: discord.Interaction):
        await interaction.response.send_modal(GrammarUI())
    
    @app_commands.command(name="wolfram", description="Provides an answer with Wolfram|Alpha")
    async def wolfram(self, interaction: discord.Interaction, query: str):
        view = wolframInitChoice(query=query)
        await interaction.response.send_message(view=view)
        view.message = await interaction.original_response()

async def setup(client):
    await client.add_cog(Cogs(client))
