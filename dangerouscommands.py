import discord

from main import client

VietKong = discord.utils.get(client.guilds, name='Viet Kong')
gulag = discord.utils.get(VietKong.roles, name='Gulag')


def gulag1(message):
    print(VietKong.roles)
    print(gulag.name)
    mem = discord.utils.get(VietKong.members, name=message.author.name)
    response = message.author.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)


def gulag2(message):
    print(gulag.name)
    target = message.content.split()[3]
    if target == 'Shimakaze': target = message.author.name
    mem = discord.utils.get(VietKong.members, name=target)
    response = mem.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)
