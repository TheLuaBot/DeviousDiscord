import discord

async def QuickEmbed(self, ctx, title, description, color=0x00ff00):
    """An Native Method of DeviousDiscord for send embeds!"""
    embed = discord.Embed(title="Your Title", description="Your Description", color=0x00ff00)