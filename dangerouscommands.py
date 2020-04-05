import discord

def gulag1(VietKong, message):
    print(VietKong.roles)
    gulag = discord.utils.get(VietKong.roles, name='Gulag')
    print(gulag.name)
    mem = discord.utils.get(VietKong.members, name=message.author.name)
    response = message.author.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)

def gulag2(VietKong, message):
    gulag = discord.utils.get(VietKong.roles, name='Gulag')
    print(gulag.name)
    target = message.content.split()[3]
    if target == 'Shimakaze': target = message.author.name
    mem = discord.utils.get(VietKong.members, name=target)
    response = mem.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)