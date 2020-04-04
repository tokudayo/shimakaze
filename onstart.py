import discord

def startupInfo(client):
	print(f'{client.user} has connected to Discord!')
	for guild in client.guilds:
		print(
			f'{client.user} is connected to the following guild:\n'
			f'{guild.name} (id: {guild.id})'
		)

    # During dev
	VietKong = discord.utils.get(client.guilds, name='Viet Kong')
	members = '\n - '.join([member.name for member in VietKong.members])
	print(f'Guild Members:\n - {members}')