from typing import Optional
import discord
from ..API.wolfram import Wolfram

class wolframPageEngine(discord.ui.View):
    def __init__(self, *, timeout=10, results=None, page=None):
        super().__init__()
        self.timeout = timeout
        self.results = results.get("pods")
        self.page = page
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    @discord.ui.button(label="Previous Subpod", style=discord.ButtonStyle.green, emoji="⬅")
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.page - 1 == 0:
            self.page -= 1
            embed = discord.Embed(title=self.results[self.page - 1].get('dataType'), color=0xFFFFFF)
            for i in self.results[self.page - 1].get("subpods"):
                embed.set_image(url=i.get("img"))
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message('You are on the first subpod.', ephemeral=True)
    
    @discord.ui.button(label='Next Subpod', style=discord.ButtonStyle.green, emoji='➡')
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.page += 1
        
        if self.page - 1 != len(self.results):
            
            embed = discord.Embed(title=self.results[self.page - 1].get('dataType'), color=0xFFFFFF)
            for i in self.results[self.page - 1].get("subpods"):
                embed.set_image(url=i.get("img"))
            await interaction.response.edit_message(embed=embed)
            
        else:
            await interaction.response.send_message('You are on the last subpod.', ephemeral=True)
            self.page -= 1

class wolframInitChoice(discord.ui.View):
    def __init__(self, *, timeout = 10, query: str):
        super().__init__()
        self.timeout = timeout
        self.query = query

    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    
    @discord.ui.button(label="Simple Answer", style=discord.ButtonStyle.green, emoji="👌")
    async def simpleans(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = Wolfram().simple(self.query)
        embed = discord.Embed(title=self.query)
        embed.set_image(url=response)

        await interaction.response.send_message(embed=embed)
    
    @discord.ui.button(label="Short Answers", style=discord.ButtonStyle.blurple, emoji="🤏")
    async def shortans(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = Wolfram().shortAnswers(self.query)
        embed = discord.Embed(title=self.query, description=response)
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="Full Results", style=discord.ButtonStyle.secondary, emoji="📜")
    async def fullres(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = Wolfram().fullResults(self.query)
        if response.get("didyoumeans") != []:  
            embed = discord.Embed(title="No results found. Did you mean: ", description="**{}**".format("\n\n".join(response.get("didyoumeans"))), color=0xFFFFFF)
            await interaction.response.send_message(embed=embed)
        else:
            pods = response.get("pods")
            embed = discord.Embed(title=pods[0].get("dataType"), color=0xFFFFFF)
            for i in pods[0].get("subpods"):
                embed.set_image(url=i.get("img"))
                view = wolframPageEngine(results=response, page=1)
            await interaction.response.send_message(view=view, embed=embed)
            view.message = await interaction.original_response()