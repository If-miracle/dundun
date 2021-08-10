# _*_ coding:utf-8 _*_

import discord, asyncio
import random

token = "ODc0MjE1Mzk0MDc0ODI0NzI0.YRDuiA.3rUvndaawtF8zcIhshMZpoPkf3E"
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("사과는 Apple 히히 :D"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    print(message.content)

    if message.content.startswith(">명령어"):
        await message.channel.send("응답")

    if message.content.startswith("에베"):
        await message.channel.send("에베베 :stuck_out_tongue_closed_eyes:")

    if message.content == ">도움말":
        embed = discord.Embed(title = "안녕하세요! 던던이에요!", description = "명령어는 아래에서 보실 수 있어요. \n\n **좋은 날 되세요!**", color = 0X79E5CB)
        embed.add_field(name="Intro", value="`dundun intro`", inline = True)
        embed.add_field(name="Game", value="`가위, 바위, 보(ㄱㅇ, ㅂㅇ, ㅂ),(ㅉ, ㅁ, ㅃ)`",inline = True)
        embed.set_footer(text = "업데이트는 제작자 마음대로\nmade by if")
        await message.channel.send(embed = embed)   

    
    if message.content == "가위" or message.content == "바위" or message.content == "보" or message.content == "ㄱㅇ" or message.content == "ㅂㅇ" or message.content == "ㅂ" or message.content == "ㅉ" or message.content == "ㅁ" or message.content == "ㅃ":
            bot_response = random.randint(1, 3)

            if bot_response == 1: 
                if message.content == "가위" or message.content == "ㄱㅇ" or message.content == "ㅉ":
                    await message.channel.send(message.author.mention + ":v: vs :v:\n비겼습니다")
                elif message.content == "바위" or message.content == "ㅂㅇ" or message.content == "ㅁ":
                    await message.channel.send(message.author.mention + ":fist: vs :v:\n제가 졌습니다")
                elif message.content == "보" or message.content == "ㅂ" or message.content == "ㅃ":
                    await message.channel.send(message.author.mention + ":hand_splayed: vs :v:\n제가 이겼습니다")
                
            elif bot_response == 2: 
                if message.content == "가위" or message.content == "ㄱㅇ" or message.content == "ㅉ":
                    await message.channel.send(message.author.mention + ":v: vs :fist:\n제가 이겼습니다")
                elif message.content == "바위" or message.content == "ㅂㅇ" or message.content == "ㅁ":
                    await message.channel.send(message.author.mention + ":fist: vs :fist:\n비겼습니다")
                elif message.content == "보" or message.content == "ㅂ" or message.content == "ㅃ":
                    await message.channel.send(message.author.mention + ":hand_splayed: vs :fist:\n제가 졌습니다")

            elif bot_response == 3: 
                if message.content == "가위" or message.content == "ㄱㅇ" or message.content == "ㅉ":
                    await message.channel.send(message.author.mention + ":v: vs :hand_splayed:\n제가 졌습니다")
                elif message.content == "바위" or message.content == "ㅁ" or message.content == "ㅁ":
                    await message.channel.send(message.author.mention + ":fist: vs :hand_splayed:\n제가 이겼습니다")
                elif message.content == "보" or message.content == "ㅂ" or message.content == "ㅃ":
                    await message.channel.send(message.author.mention + ":hand_splayed: vs :hand_splayed:\n비겼습니다")

@client.event
async def on_message_delete(message):
    await message.channel.send("메세지 삭제가 감지 되었습니다.`" + str(message.author) + ":" + message.content + "`")
    return        
    
client.run(token)