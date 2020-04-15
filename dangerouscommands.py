import discord

async def gulag1(message):
    guild = message.guild
    print(guild.roles)
    gulag = discord.utils.get(guild.roles, name='Gulag')
    print(gulag.name)
    mem = discord.utils.get(guild.members, name=message.author.name)
    response = message.author.mention + " Con chó này cho vào gulag"
    await message.channel.send(response)
    await mem.add_roles(gulag)


async def gulag2(user, message):
    guild = message.guild
    gulag = discord.utils.get(guild.roles, name='Gulag')
    print(gulag.name)
    target = message.content.split()[3]
    if target == user.name: target = message.author.name
    try:
        mem = discord.utils.get(guild.members, name=target)
        response = mem.mention + " Con chó này cho vào gulag"
        await message.channel.send(response)
        await mem.add_roles(gulag)
    except:
        await message.channel.send("Thằng đầu buồi, làm đ có ai tên như thế ở đây.")
