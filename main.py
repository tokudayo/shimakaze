import os

from dotenv import load_dotenv
from onstart import *
from responses import *
from dangerouscommands import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
VietKong = discord.Guild

@client.event
async def on_ready():
    startupInfo(client)
    #during dev:
    global VietKong
    VietKong = discord.utils.get(client.guilds, name='Viet Kong')
    #end


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user: return

    await mentionResponse(client.user, message)
    await swearResponse(message)
    await keywordResponse(message)
    await jokeResponse(message)

    if 'bác tài' in message.content.lower():
        await gulag1(message)
    if message.content.lower().startswith("cho con chó") and 'gulag' in message.content.lower():
        await gulag2(client.user, message)


@client.event
async def on_message_delete(message):
    responses = [
        message.author.mention + " Mày đang giấu cái gì thế",
        message.author.mention + " very ninja delete",
        message.author.mention + " ninja delete <:pepeW:687878953419145296>"
    ]
    response = random.choice(responses)
    if not message.author.bot: await message.channel.send(response)


client.run(TOKEN)
