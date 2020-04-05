import random

mentionResponses = [
    'Để yên cho bố thủ dâm',
    'Vào thủ dâm cùng tao ko? ( ͡° ͜ʖ ͡°)',
    'https://hanime.tv/hentai-videos/oni-chichi-1-episode-1',
]

swearResponses = [
    f'Chửi thề con cặc nói chuyện vô văn hóa',
    (
        'Tao có súng đây này\n'
        'Chửi thề là tao bắn mày á'
    ),
    'địt mẹ nhà mày, bố mẹ dạy mày kiểu đéo j đấy cái thg chó vô văn hóa kia',
]

swearWords = [
    'cặc',
    'địt',
    'lồn'
]

keywordResponses = [
    ['duy ko làm bài tập', 'Thằng nát này <:pepeW:687878953419145296>'],
    ['tài', 'Gọi bác thêm lần nữa là kick'],
    ['đen', 'phân biệt chủng tộc ăn cac'],
    ['nigga', 'phân biệt chủng tộc ăn cac'],
    ['compe', 'đmm bố mày đang học'],
    ['nát', 'nát'],
]


async def mentionResponse(client, message):
    if client.user.mentioned_in(message):
        response = random.choice(mentionResponses)
        await message.channel.send(response)


async def swearResponse(client, message):
    for word in swearWords:
        if word in message.content.lower():
            response = random.choice(swearResponses)
            response = message.author.mention + " " + response
            await message.channel.send(response)
            break


async def keywordResponse(client, message):
    for trigger in keywordResponses:
        reply = True
        for word in trigger[0].split():
            if word not in message.content.lower():
                reply = False
                break
        if reply: await message.channel.send(trigger[1])


async def jokeResponse(client, message):
    if message.channel.name == 'nsfw':
        if message.author.id == 215806040900501505:
            await message.channel.send('địt mẹ cái thg đồi trụy')
        if message.author.id == 274866353586962433:
            await message.channel.send('furry <:pepeW:687878953419145296>')

    if (message.channel.name == 'general' or message.channel.name == 'trash') and 'anime' in message.content.lower():
        await message.channel.send(message.author.mention + ' fucking weeb <:pepeW:687878953419145296>')

    if 'good' in message.content and 'bot' in message.content:
        await message.channel.send('Lick my ass, Onii-chan **OwO**')
