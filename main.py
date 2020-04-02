import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	for guild in client.guilds:
		print(
			f'{client.user} is connected to the following guild:\n'
			f'{guild.name} (id: {guild.id})'
		)

	#During dev
	VietKong = discord.utils.get(client.guilds, name='Viet Kong')
	members = '\n - '.join([member.name for member in VietKong.members])
	print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if client.user.mentioned_in(message):
		await message.channel.send('Để yên cho bố thủ dâm')

	responses = [
		f'Chửi thề con cặc nói chuyện vô văn hóa',
		(
			'Tao có súng đây này\n'
			'Chửi thề là tao bắn mày á'
		),
	]

	curse = ['cặc', 'địt']

	for word in curse:
		if word in message.content.lower():
			response = random.choice(responses)
			response = message.author.mention + response
			await message.channel.send(response)
			break


	Response = [
		['duy ko làm bài tập', 'Thằng nát này <:pepeW:687878953419145296>'],
		['tài', 'Tài là thằng nào tao ko quen'],
	]

	for trigger in Response:
		if trigger[0] in message.content.lower():
			await message.channel.send(trigger[1])

client.run(TOKEN)