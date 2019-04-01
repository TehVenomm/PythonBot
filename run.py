import discord
from discord.ext import commands
import myUtilities
import secrets

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def roleonline(ctx, *a):
	role = discord.utils.get(ctx.guild.roles, name="A")
	for user in ctx.guild.members:
		if (user.has_role(role)):
			print('nope')
		else: 
			await user.add_roles(role)

bot.run(secrets.getToken(), bot=False)