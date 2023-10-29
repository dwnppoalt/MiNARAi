from ..API.grammar import Grammar
from discord import ui
import discord

class GrammarUI(ui.Modal, title='Questionnaire Response'):
    text = ui.TextInput(label="Text", placeholder = "A quick brown fox jumps over the lazy dog")
    async def on_submit(self, interaction: discord.Interaction):
        proofread = Grammar().grammar(text=self.text)
        embed = discord.Embed(colour=0x1abc9c)
        embed.add_field(name="Original", value=self.text, inline=False)
        embed.add_field(name="Proofread", value=proofread, inline=False)
        embed.set_author(name=f"Requested by: {interaction.user.display_name}", icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)

