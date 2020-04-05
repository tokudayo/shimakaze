import discord

async def gulag1(client, guild, message):
    print(guild.roles)
    gulag = discord.utils.get(guild.roles, name='Gulag')
    print(gulag.name)
    mem = discord.utils.get(guild.members, name=message.author.name)
    response = message.author.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)


async def gulag2(client, guild, message):
    gulag = discord.utils.get(guild.roles, name='Gulag')
    print(gulag.name)
    target = message.content.split()[3]
    if target == client.user: target = message.author.name
    mem = discord.utils.get(guild.members, name=target)
    response = mem.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)
