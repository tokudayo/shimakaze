import os
import random
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()

FFMPEG = os.getenv('FFMPEG')

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
    'lồn',
    'buồi',
    'cằc',
    'đụ',
    'ching chong'
]

keywordResponses = [
    ['duy ko làm bài tập', 'Thằng nát này <:pepeW:687878953419145296>'],
    ['tài', 'Gọi bác thêm lần nữa là kick'],
    ['đen', 'phân biệt chủng tộc ăn cac'],
    ['nigga', 'phân biệt chủng tộc ăn cac'],
    ['compe', 'đmm bố mày đang học'],
    ['nát', 'nát'],
    ['f', 'https://tenor.com/view/press-f-pay-respect-keyboard-gif-12855017'],
    ['x', 'Doubt'],
    ['y', 'Shame'],
    ['"y"', 'same'],
]

randomResponses = [
    "Did you ever hear the tragedy of Kanna the dragon loli? I thought not, it's not a story Sagiri fans would tell you.\n\n"\
    "It's a legend of the lolicons...\n\n\n\n\n\n\n\n"\
    "Kanna the dragon loli was a gothic loli from the other world."\
    " So powerful and cute she could use the force to influence the other school kids to win sports festivals..."\
    " She had such a knowledge of the loli side that she could even keep the ones she cared about from growing up.\n\n"\
    "She could actually save people from growing up?\n\n"\
    "The loli side is a pathway to many abilities some consider to be...immoral.\n\n"\
    "What happened to her?\n\n"\
    "She became so powerful... the only thing she was afraid of was growing up, which eventually of course, she did."\
    " Unfortunately, she taught her apprentice everything she knew. Then her apprentice made her a woman in her sleep."\
    " Ironic, she could save others from growing up, but not herself.",

    "I swear, every time I bring a girl home,"\
    " I make sure to clean everything up in my room and take special care to ensure that my 5352 ranked core mmr is prominently on display,"\
    " with mid ticked and ready to go with my dual monitor displaying my DotaBuff account."\
    " But then when we get into my room, she just pushes me to the bed and starts making out with me right away."\
    " Like, did you not notice my win streak? I didnt bring you here to make out."\
    " I want you to experience the insane APM, the perfect CS, and the dead mid towers around the 8 minute mark."\
    " I bet I play way better than your party friends."\
    " Trust me, you havent experienced true skill until you try playing - wait where are you going?",

]


async def mentionResponse(user, message):
    if user.mentioned_in(message):
        response = random.choice(mentionResponses)
        await message.channel.send(response)


async def swearResponse(message):
    for word in swearWords:
        if word in message.content.lower():
            response = random.choice(swearResponses)
            response = message.author.mention + " " + response
            await message.channel.send(response)

            response = message.author.mention + " vào voice bố bảo"
            await message.channel.send(response)
            await asyncio.sleep(8)

            VietKong = message.guild
            voice = discord.utils.get(VietKong.voice_channels, name='voice?')
            if message.author not in voice.members:
                await message.channel.send(message.author.mention + " Đm con chó này sợ ko dám vào à <:KEKW:687878492058026027>")
            else:
                try:
                    vc = await voice.connect()
                    vc.play(discord.FFmpegPCMAudio(executable=FFMPEG, source='audio/cac.mp3'))
                    while vc.is_playing():
                        await asyncio.sleep(10)
                    await vc.disconnect()
                except:
                    gulag = discord.utils.get(message.guild.roles, name='Gulag')
                    mem = message.author;
                    await message.channel.send(message.author.mention + " Cho vào gulag ngồi nghĩ về cuộc đời <:pepeW:687878953419145296>")
                    await mem.add_roles(gulag)
                    #await message.channel.send(message.author.mention + "Mày làm tao crash rồi chửi ít thôi con chó <:pepeW:687878953419145296>")

            break


async def keywordResponse(message):
    for trigger in keywordResponses:
        reply = True
        for word in trigger[0].split():
            if word not in message.content.lower():
                reply = False
                break
        if reply: await message.channel.send(trigger[1])


async def jokeResponse(message):
    if message.channel.name == 'nsfw':
        if message.author.id == 215806040900501505:
            await message.channel.send('địt mẹ cái thg đồi trụy')
        if message.author.id == 274866353586962433:
            await message.channel.send('furry <:pepeW:687878953419145296>')

    if (message.channel.name == 'general' or message.channel.name == 'trash') and 'anime' in message.content.lower():
        await message.channel.send(message.author.mention + ' fucking weeb <:pepeW:687878953419145296>')

    if 'good' in message.content and 'bot' in message.content:
        await message.channel.send('Lick my ass, Onii-chan **OwO**')


async def randomResponse(message):
    lotto = random.choice(range(1, 50))
    if lotto == 25:
        response = random.choice(randomResponses)
        await message.channel.send(response)
