import discord, asyncio, random, time
import os
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ㅈㅅ봇베타"))

@client.event
async def on_message(message):
    if message.content == "!ㅈㅅ 안녕":
        await message.channel.send("안녕하세요")

    if message.content == "!ㅈㅅ ㅈㅅ":
        await message.channel.send("저의 기획자에요!")

    if message.content == "!ㅈㅅ gosato1234":
        await message.channel.send("저의 개발자에요!")

    if message.content == "!ㅈㅅ 사토":
        await message.channel.send("저의 개발자에요!")

    if message.content == "!ㅈㅅ 가위":
        rand = random.randint(0,2)
        if rand == 0:
            await message.channel.send("가위(비김)")
        if rand == 1:
            await message.channel.send("바위(짐)")
        if rand == 2:
            await message.channel.send("보(이김)")
    
    if message.content == "!ㅈㅅ 바위":
        rando = random.randint(0,2)
        if rando == 0:
            await message.channel.send("가위(이김)")
        if rando == 1:
            await message.channel.send("바위(비김)")
        if rando == 2:
            await message.channel.send("보(짐)")

    if message.content == "!ㅈㅅ 보":
        randmo = random.randint(0,2)
        if randmo == 0:
            await message.channel.send("가위(짐)")
        if randmo == 1:
            await message.channel.send("바위(이김)")
        if randmo == 2:
            await message.channel.send("보(비김)")




    if message.content == "!ㅈㅅ 임베드":
        embed = discord.Embed(title="ㅈㅅ봇", description="베타버전", color=0x00ff00)
        embed.set_footer(text='봇제작자.gosato1234 #1472', icon_url="https://cdn.discordapp.com/attachments/917771765080547331/942677125234847804/E3657R1VUAQknJ8.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/942301955190054925/942670961398935594/57_20220212201239.jpg")
        embed.add_field(name="명령어", value="!ㅈㅅ을 쓰고 사용해주세요", inline=False)
        embed.add_field(name="창시일", value="2022-02-14", inline=False)
        embed.add_field(name="제작자", value="gosato1234#1472", inline=False)
        embed.add_field(name="기획자", value="ㅈㅅ#1101", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "!ㅈㅅ 뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            await message.channel.send("꽝")
        if ran == 1:
            await message.channel.send("당첨")
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
