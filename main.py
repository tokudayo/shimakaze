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

    # During dev
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

    curse = ['cặc', 'địt', 'lồn']

    for word in curse:
        if word in message.content.lower():
            response = random.choice(responses)
            response = message.author.mention + response
            await message.channel.send(response)
            break

    Response = [
        ['duy ko làm bài tập', 'Thằng nát này <:pepeW:687878953419145296>'],
        ['tài', 'Gọi bác thêm lần nữa là kick'],
        ['đen', 'phân biệt chủng tộc ăn cac'],
        ['nigga', 'phân biệt chủng tộc ăn cac'],
        ['compe', 'đmm bố mày đang học'],
        ['nát', 'nát'],
    ]

    for trigger in Response:
        reply = True
        for word in trigger[0].split():
            if word not in message.content.lower():
                reply = False
                break
        if reply: await message.channel.send(trigger[1])

#    if 'corona' in message.content.lower():
#        cough =
#        selfVoice = discord.VoiceChannel.connect()
#        selfVoice.play(cough)

    VietKong = discord.utils.get(client.guilds, name='Viet Kong')
    if 'bác tài' in message.content.lower():
        print(VietKong.roles)
        gulag = discord.utils.get(VietKong.roles, name='Gulag')
        print(gulag.name)
        mem = discord.utils.get(VietKong.members, name=message.author.name)
        admin = discord.utils.get(VietKong.members, name=client.user.name)
        response = message.author.mention + " Con chó này cho vào gulag"
        await message.channel.send(response)
        await mem.add_roles(gulag)

    if message.content.lower().startswith("cho con chó") and 'gulag' in message.content.lower():
        gulag = discord.utils.get(VietKong.roles, name='Gulag')
        print(gulag.name)
        target = message.content.split()[3]
        if target == 'Shimakaze': target = message.author.name
        mem = discord.utils.get(VietKong.members, name=target)
        response = mem.mention + " Con chó này cho vào gulag"
        await message.channel.send(response)
        await mem.add_roles(gulag)


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
