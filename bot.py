import discord
import asyncio
import aiohttp
import string
import random
import datetime
import os

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("디스코드 봇 작동을 시작합니다.")
    print("봇 아이디: " + bot.user.id)
    print("=============================")
    await bot.change_presence(game=discord.Game(name="!명령어 Made by 5.56mm",
                                                type=1))


@bot.command(pass_context=True)
async def 명령어(ctx):
    now = datetime.datetime.now()
    embed = discord.Embed(title="❄ 명령어 목록 ❄", description="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", color=0x00ff80)
    embed.add_field(name="!명령어", value="해당 메세지를 한번 더 확인합니다.", inline=False)
    embed.add_field(name="!채팅청소 [숫자]", value="14일 이내에 기록되었던 채팅을 [숫자] 만큼 삭제합니다. (범위: 1~100)", inline=False)
    embed.add_field(name="!초대링크", value="5분 뒤 파기되는 초대링크를 생성합니다. [관리자 권한 필요]", inline=False)
    embed.add_field(name="!공지 [#텍스트채널] [시간(단위:분)] [할말]", value="텍스트채널에 [시간] 간격으로 [할말]을 전송합니다. [관리자 권한 필요]",
                    inline=False)
    embed.add_field(name="!투표 [주제]", value="[주제]라는 주제로 투표를 생성합니다.", inline=False)
    embed.add_field(name="!투표결과", value="진행중인 투표의 중간 결과를 확인합니다.", inline=False)
    embed.add_field(name="!투표확인", value="진행중인 투표를 마감시키고 결과를 확인합니다.", inline=False)
    embed.add_field(name="!오피지지", value="opgg 링크를 보내줍니다.", inline=False)
    embed.add_field(name="!배그", value="배틀그라운드 페이지를 보내줍니다.", inline=False)
    embed.add_field(name="~배그 [닉네임] [카/스] [솔/듀/스]", value="ex) ~배그 a_va82p 카 듀 │ 배틀그라운드 전적검색을 해준다.", inline=False)
    embed.add_field(name="~주사위", value="주사위를 무작위로 굴립니다.", inline=False)
    embed.add_field(name="~날씨 [지역]", value="날씨를 알려줍니다.", inline=False)
    embed.add_field(name="~가르치기 [단어],[설명]", value="매화봇이 단어를 기억합니다", inline=False)
    embed.add_field(name="~말해 [단어]", value="기억한 단어를 알려줍니다.", inline=False)
    embed.add_field(name="~골라 [항목1],[항목2],[항목n...]", value="항목 하나를 랜덤으로 고릅니다.", inline=False)
    embed.add_field(name="=m p [음악]", value="음악을 틀어줍니다(음성채널 안에서 실행됨)", inline=False)
    embed.add_field(name="=m l", value="Ayana를 음성채널에서 내보냅니다.", inline=False)
    embed.add_field(name="=m s", value="현재 듣고 있는 노래를 스킵합니다.", inline=False)
    embed.add_field(name="=m q", value="음악 리스트를 보여줍니다", inline=False)
    embed.add_field(name="=m pg", value="음악 리스트를 삭제합니다.", inline=False)
    embed.set_footer(text="•"+(str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" "+"Made by 5.56mm#1944•"))
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def 초대링크(ctx):
    '''사용법: !초대링크'''
    try:
        link = await bot.create_invite(ctx.message.channel, max_age=300, max_uses=0)
        await bot.say(link)

    except discord.HTTPException:
        await bot.say("초대 링크를 생성하지 못했습니다. 다시 시도해주세요.")


@bot.command(pass_context=True)
async def 채팅청소(ctx, amount=100):
    '''사용법: !채팅청소 [개수]'''
    '''[개수]에는 1보다 크고 100보다 작은 자연수가 들어가야합니다.'''
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    embed = discord.Embed(title="메세지 제거완료", description="{}개의 메세지가 제거되었습니다.".format(len(messages)),
                          color=0xffffff)  # 몇개의 메세지가 제거되었는지 출력
    embed.add_field(name="처리자: ", value="<@%s>" % (ctx.message.author.id),
                    inline=False)  # 해당 구문은 지워도 상관 없습니다. (채팅청소 명령어 친사람 출력)
    await bot.say(embed=embed)


# 명령어: 공지
@bot.command(pass_context=True)
async def 공지(ctx, channel: discord.Channel, timeout: int, *args):
    '''사용법: !공지 [#채팅 채널 이름] [반복주기 단위:분] [할말]'''
    '''중간에 끄시려면 봇을 껐다키세요'''
    output = ''
    try:
        if ctx.message.author.server_permissions.administrator:  # 관리자 권한 구문입니다. 관리자/일반유저 권한을 없애고 싶으시다면 이 메세지와 밑의 else ~ await bot.say까지 지워주시고, try와 except로 시작하는 구문을 제외하고 모든 구문을 왼쪽으로 4칸씩 옮겨야 합니다.
            author = ctx.message.author.id
            for word in args:
                output += word
                output += ' '
            value = 0
            while value < 1:
                await bot.say(output)
                await asyncio.sleep(timeout * 60)
        else:
            await bot.say("당신은 해당 명령어를 사용할 권한이 없습니다.")  # 권한이 없을 때 출력되는 메세지를 여기서 변경하실 수 있습니다. (텍스트 사이에 " 꼭 넣어주세요!)
    except Exception as announce:
        await bot.say('오류가 발생하였습니다. \n[{}]'.format(announce))

#명령어: 투표
@bot.command(pass_context=True)
async def 투표(ctx, *, question: str = None):
    '''구문이 좀 어려워서 웬만하면 손 안대시는걸 추천드립니다 ^^;;'''
    '''사용법: !투표 [주제]'''
    if question:
        max_options = 10
        max_wait_time = 86400  #자동 마감 시간을 설정하실 수 있습니다. (기본설정: 1일)

        prompt1 = await bot.say("투표 선택지를 입력하세요. 완료하셨으면 'x'를 입력해주세요.")
        reply = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                           channel=ctx.message.channel)
        number_of_options = 0
        options = ""
        replies = []
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
        while reply.content != 'x' and number_of_options < max_options:
            replies.append(reply)
            options += reactions[number_of_options] + "  " + reply.content + "\n"
            number_of_options += 1
            reply = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                               channel=ctx.message.channel)
        if number_of_options <= 1:
            await bot.say(
                "2개 이상의 선택지를 입력해주세요.")
            return

        prompt2 = await bot.say(
            "투표 자동 마감시간을 설정해주세요. (단위: 분) \n0은 무제한입니다.")
        wait = await get_poll_time(ctx, max_wait_time)

        if wait.content == "0":
            poll_message = await bot.say("=== **투표** ===\n❓**:** " + question + "\n\n" + options
                                         + "\n\n*#투표마감 으로 투표를 마감하세요.\n#투표확인 으로 진행중인 투표 결과를 확인하세요.*")
            for reaction in reactions[:number_of_options]:
                await bot.add_reaction(poll_message, reaction)
            await cleanup(reply, replies, ctx, prompt1, prompt2)
            message = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                                 channel=ctx.message.channel)
            while message is not None and message.content != "!투표마감":
                if message.content == "!투표확인":
                    try:
                        await bot.delete_message(message)
                    except Exception as e:
                        print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                        print(e)
                    await post_results(ctx, poll_message, replies, reactions, number_of_options, question)
                    message = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                                         channel=ctx.message.channel)
                else:
                    message = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                                         channel=ctx.message.channel)
            try:
                await bot.delete_message(message)
            except Exception as e:
                print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                print(e)
        else:
            poll_message = await bot.say("=== **투표** ===\n❓**:** " + question + "\n\n" + options)
            for reaction in reactions[:number_of_options]:
                await bot.add_reaction(poll_message, reaction)
            await cleanup(reply, replies, ctx, prompt1, prompt2)
            await asyncio.sleep(int(wait.content) * 60)
        await post_results(ctx, poll_message, replies, reactions, number_of_options, question)
    else:
        await bot.say("사용법: !투표 [주제]")

async def cleanup(reply, replies, ctx, prompt1, prompt2):
    try:
        await bot.delete_message(reply)
        for reply in replies:
            await bot.delete_message(reply)
        await bot.delete_message(ctx.message)
        await bot.delete_message(prompt1)
        await bot.delete_message(prompt2)
    except Exception as e:
        print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
        print(e)

async def post_results(ctx, poll_message, replies, reactions, number_of_options, question):
    cache_msg = discord.utils.get(bot.messages, id=poll_message.id)
    counts = []
    var1 = 0
    for reaction in cache_msg.reactions[:number_of_options]:
        reactors = await bot.get_reaction_users(reaction)
        counts.append(-1)
        for reactor in reactors:
            counts[var1] += 1
        var1 += 1

    highest = 0
    for count in counts:
        if count > highest:
            highest = count

    var1 = 0
    results = ""
    while var1 < len(counts):
        if counts[var1] == highest and counts[var1] > 1:
            results += reactions[var1] + "  " + replies[var1].content + " - **" + str(
                counts[var1]) + "** 표  :white_check_mark:" + "\n"
        elif counts[var1] == highest and counts[var1] == 1:
            results += reactions[var1] + "  " + replies[var1].content + " - **" + str(
                counts[var1]) + "** 표  :white_check_mark:" + "\n"
        elif counts[var1] != highest and counts[var1] == 1:
            results += reactions[var1] + "  " + replies[var1].content + " - **" + str(counts[var1]) + "** 표\n"
        else:
            results += reactions[var1] + "  " + replies[var1].content + " - **" + str(counts[var1]) + "** 표\n"
        var1 += 1

    embed = discord.Embed(title="\n투표 결과", description="\n생성자: <@" + str(ctx.message.author.id) + ">", color=0xffffff)
    embed.add_field(name="\n❓**:** " + question, value="\n\n" + results, inline=False)
    await bot.say(embed=embed)

async def get_poll_time(ctx, max_wait_time):
    wait = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author, channel=ctx.message.channel)
    while not wait.content.isdigit() or int(wait.content) > max_wait_time:
        if not wait.content.isdigit():
            ans = await bot.say("숫자만 입력해주세요.")
            try:
                await bot.delete_message(wait)
            except Exception as e:
                print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                print(e)
            wait = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                              channel=ctx.message.channel)
            try:
                await bot.delete_message(ans)
            except Exception as e:
                print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                print(e)
        elif int(wait.content) > max_wait_time:
            ans = await bot.say("최대 마감시간을 1일 이하로 설정해주세요.")
            try:
                await bot.delete_message(wait)
            except Exception as e:
                print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                print(e)
            wait = await bot.wait_for_message(timeout=max_wait_time, author=ctx.message.author,
                                              channel=ctx.message.channel)
            try:
                await bot.delete_message(ans)
            except Exception as e:
                print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
                print(e)
    try:
        await bot.delete_message(wait)
    except Exception as e:
        print("메세지를 삭제하는 동안 오류가 발생하였습니다.")
        print(e)
    return wait


@bot.command(pass_context=True)
async def 오피지지(ctx):
    now = datetime.datetime.now()
    embed = discord.Embed(title="OP.GG", description="- - - - - - - - - - - - - - - - - - - - - -", color=0x00ff80)
    embed.add_field(name="리그 오브 레전드 OP.GG", value="https://www.op.gg", inline=False)
    embed.add_field(name="배틀그라운드 OP.GG", value="https://pubg.op.gg", inline=False)
    embed.add_field(name="오버워치 OP.GG", value="https://overlog.gg/", inline=False)
    embed.set_footer(text="•"+(str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" "+"Made by 5.56mm#1944•"))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def 배그(ctx):
    now = datetime.datetime.now()
    embed = discord.Embed(title="배틀그라운드", description="- - - - - - - - - - - - - - - - - - - - - -", color=0x00ff80)
    embed.add_field(name="카카오 배틀그라운드", value="http://pubg.game.daum.net/pubg/index.daum", inline=False)
    embed.add_field(name="배틀그라운드 공식 페이지", value="https://www.pubg.com/ko/", inline=False)
    embed.set_footer(text="•" + (str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " " + "Made by 5.56mm#1944•"))
    await bot.say(embed=embed)


access_token = os.environ["BOT_TOKEN"]
bot.run(access_tokken)
