import setting
import discord
import asyncio
import random
import time
from urllib.request import urlopen, Request
import urllib
import bs4
from urllib.request import Request
import openpyxl
import re
import requests
from bs4 import BeautifulSoup
import datetime
import os
import sys
import json
from selenium import webdriver
set = setting.set()


app = discord.Client()
times = int(time.time())


maker = "480568196286644224"


@app.event
async def on_ready():
    print("login")
    print(app.user.name)
    print(app.user.id)
    print("------------------")
    await app.change_presence(game=discord.Game(name='_도움말', type=0))
    
@app.event
async def on_message(message):

     id = message.author.id
     channel = message.channel
     owner = ['480568196286644224','536133196706873352','562640781379239937']
     if message.author.bot:
          return None

     if message.content.startswith("문서작성기"):
         await app.send_message(message.channel, '첫줄')
         d = await app.wait_for_message(timeout=30, author=message.author)
         d = d.content
         await app.send_message(message.channel, "두줄")
         a = await app.wait_for_message(timeout=30, author=message.author)
         a = a.content
         await app.send_message(message.channel, "세줄")
         b = await app.wait_for_message(timeout=30, author=message.author)
         b = b.content
         await app.send_message(message.channel, "네줄")
         c = await app.wait_for_message(timeout=30, author=message.author)
         c = c.content
         await app.send_message(message.channel, "파일이름(영어로 해야 파일이름 오류가 없습니다.)")
         n = await app.wait_for_message(timeout=30, author=message.author)
         n = n.content         
         
         
         file = open(n + ".txt", "w")
         file.write("제작 : ! ㈜인 찾음#6686\n\n"
                    "문서작성기\n\n"    
                    "첫줄 : " + d + "\n\n"
                    "두줄 : " + a + "\n\n"         
                    "세줄 : " + b + "\n\n"
                    "네줄 : " + c + "")
         
         file.close()
                  
         await app.send_file(message.channel, n + ".txt")
	
     if message.content.startswith('_DM'):
        if id in owner:     
            member = discord.utils.get(app.get_all_members(), id=message.content[4:22])
            await app.send_message(member, message.content [23:])
        else:
            await app.send_message(channel,'권한이 있어야 합니다!')
	
	
     if message.content.startswith('_say'):         
         learn = message.content.replace('_say', "")
         await app.send_message(message.channel,learn+'')     

    
     if message.author.id == app.user.id: return
	
     if message.content.startswith("_채널"):
        if id in owner:              
            channel = app.get_channel(id=message.content[4:22])
            await app.send_message(channel, message.content[23:])            
        else:
            await app.send_message(channel,'권한이 있어야 합니다!')	

     if message.content.startswith("_로그"):
        if id in owner:
            channel = app.get_channel(id=message.content[4:22])
            embed = discord.Embed(title="로그 전송 안내", description='로그 내용:' + message.content[22:],color=0x19deff)
            embed.set_footer(text="로그 일부분만 보내 드립니다.")
            await app.send_message(channel, embed=embed)
        else:
            await app.send_message(channel,'권한이 있어야 합니다!')

     if message.content.startswith("_원격"):
        if id in owner:         
            channel = app.get_channel(id=message.content[4:22])
            embed = discord.Embed(title="원격 시스템", description=message.content[23:],color=0x19deff)
            await app.send_message(channel, embed=embed)
        else:
            await app.send_message(channel,'권한이 있어야 합니다!')	
	
     if message.content.startswith('응아아오여ㅗㅕㅑㅠㄷ소ㅑ즂'):
        await app.send_message(channel, 'ㅂㅈㅅㅂㅈㅅㅎㄷ') 
     else: 
               embed = discord.Embed(
                   title = '통합로그',
                   description = "채널이름: %s(%s) | 유저네임: %s(#%s) | 메시지: %s" % (message.channel, str(message.channel.id)[:5],message.author.name, str(message.author.id),message.content),
                   colour = discord.Colour.blue()
               )	
               channel1 = discord.Object(id='563886078587568150')
               await app.send_message(channel1,embed=embed)

	

     if message.content.startswith('_ping'):
         before = time.monotonic()
         msg = await app.send_message(message.channel, '핑측정중...')
         ping = (time.monotonic() - before) * 1000
         text = ":ping_pong:!  {0}ms".format((round(ping,1)))
         embed = discord.Embed(title='핑',description=text,color=0x00ff00)
         await app.edit_message(msg,embed=embed)
	
     if message.content.startswith('소유자도움말'):
          await app.send_message(channel,'DM으로 보냈습니다!')
          member = discord.utils.get(app.get_all_members(),id=message.author.id)
          embed = discord.Embed(
            title = '소유자 도움말 입니다.',
            description = '아무나 못써요!',
            colour = discord.Colour.blue()
          )
          embed.add_field(name='_봇게임', value = '이메시지 생성!',inline = False)
          embed.add_field(name='_로그', value = '다른서버에 메시지를 보냄!',inline = False)
          embed.add_field(name='_채널', value = '다른서버에 메시지를 보냄!',inline = False)
          embed.add_field(name='_원격', value = '다른서버에 메시지를 보냄!',inline = False)
          embed.add_field(name='공지', value = '다른서버에 공지를 보냄!',inline = False)
          embed.add_field(name='_따라해', value = '현재 채널에 메시지를 ',inline = False)	
          embed.add_field(name='_DM', value = '사람한데 메시지를 보냄',inline = False)	
          await app.send_message(member, embed=embed)		
		
	
     if message.content.startswith('_도움말'):
          await app.send_message(channel,'DM으로 보냈습니다!')
          member = discord.utils.get(app.get_all_members(),id=message.author.id)
          embed = discord.Embed(
            title = '봇의 기능들입니다.',
            description = '명령어가 너무 적어서 따로 적었어용!',
            colour = discord.Colour.blue()
          )
          embed.add_field(name='_도움말', value = '이메시지 생성!',inline = False)
          embed.add_field(name='_업타임', value = '봇이 켜진시간 확인!',inline = False)
          embed.add_field(name='_날씨 지역', value = '날씨확인',inline = False)
          embed.add_field(name='_미세먼지', value = '미세먼지확인',inline = False)
          embed.add_field(name='_초미세먼지', value = '초미세먼지확인',inline = False)
          embed.add_field(name='_정보', value = '자신의 정보확인',inline = False)
          embed.add_field(name='_say', value = '봇이 말을 따라함!',inline = False)
          embed.add_field(name='_프로필 @멘션', value='프로필을 보여줌', inline=False)
          await app.send_message(member, embed=embed)		

	
     if message.content.startswith('_봇게임'):
        if id in owner:         
           learn = message.content.replace('_봇게임', "")
           await app.change_presence(game=discord.Game(name=learn))
           await app.send_message(message.channel, "봇의 플래이중을 바꿨습니다.")
        else:
           await app.send_message(channel,'')
	





     if message.content.startswith('_업타임'):
          a = int(time.time())
          await app.send_message(channel,str(a-times)+'초')

	

        
     if message.content.startswith('_따라해'):
        if id in owner:
           await app.delete_message(message)            
           learn = message.content.replace('_따라해', "")
           await app.send_message(message.channel,learn+'')     
        else:
           await app.send_message(channel,'')

     if message.content.startswith('_날씨'):
        try:
            embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
            meg = await app.send_message(channel,embed=embed)
            learn = message.content.split(" ")
            location = learn[1]
            enc_location = urllib.parse.quote(location+'날씨')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bs_obj = bs4.BeautifulSoup(html, "html.parser")
            div = bs_obj.find("span",{"class":'todaytemp'})
            div2 = bs_obj.find("p",{"class":"cast_txt"})
            embed = discord.Embed(title=location+'날씨',description=div.text+'℃'+'\n'+div2.text+'\n'+'네이버 날씨',color=0x00ff00)
            await app.edit_message(meg,embed=embed)
        except:
           await app.send_message(channel,'없는 도시입니다!')
            
     if message.content.startswith('_미세먼지'):
        try:
           embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
           meg = await app.send_message(channel,embed=embed)
           learn = message.content.split(" ")
           location = learn[1]
           enc_location = urllib.parse.quote(location+'미세먼지')
           hdr = {'User-Agent': 'Mozilla/5.0'}
           url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
           req = Request(url, headers=hdr)
           html = urllib.request.urlopen(req)
           bs_obj = bs4.BeautifulSoup(html, "html.parser")
           div = bs_obj.find("em",{"class":'main_figure'})
           div2 = bs_obj.find("span",{'class':'update'})
           learn2 = int(div.text)
           if learn2 < 16:
               a = '최고'
           elif learn2 < 31:
               a = '좋음'
           elif learn2 < 41:
               a = '양호'
           elif learn2 < 51:
               a = '보통'
           elif learn2 < 76:
               a = '나쁨'
           elif learn2 < 101:
               a = '상당히 나쁨'
           elif learn2 < 151:
               a = '매우나쁨'
           elif learn2 > 150:
               a = '최악'
           embed = discord.Embed(title=learn[1]+'미세먼지',description='**'+str(learn2)+'㎍/㎥ \n'+a+'**\n'+div2.text+'\n'+'네이버 미세먼지/미세먼지 기준 미세미세8단계',color=0x00ff00)
           await app.edit_message(meg,embed=embed)
        except:
            await app.send_message(channel,'없는 도시 거나 도/시는 미세먼지 검색이 안됩니다.')

     if message.content.startswith('_청소'):
        if id in owner:    
             learn = message.content.split(' ')
             mgs = []
             number = int(learn[1])
             async for x in app.logs_from(message.channel, limit = number+1):
                  mgs.append(x)
             await app.delete_messages(mgs)
             delembed = discord.Embed(title=":speech_left: 메세지 삭제됨. (이 메세지는 3초 후 삭제됩니다)",color=0x4286f4)
             delmsg = await app.send_message(channel,embed = delembed)
             await asyncio.sleep(3)
             await app.delete_message(delmsg)	
        else:
            await app.send_message(message.channel, "당신은 권한이 없습니다!")    	
	
     if message.content.startswith('_초미세먼지'):
            learn = message.content.split(' ')
            embed = discord.Embed(title='잠시만요',description='불러오고있습니다!',color=0x00ff00)
            meg = await app.send_message(channel,embed=embed)
            location = learn[1]
            enc_location = urllib.parse.quote(location+'초미세먼지')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bs_obj = bs4.BeautifulSoup(html, "html.parser")
            div = bs_obj.find("em",{"class":'main_figure'})
            div2 = bs_obj.find("span",{'class':'update'})
            learn2 = int(div.text)
            if learn2 < 16:
                a = '최고'
            elif learn2 < 31:
                a = '좋음'
            elif learn2 < 41:
                a = '양호'
            elif learn2 < 51:
                a = '보통'
            elif learn2 < 76:
                a = '나쁨'
            elif learn2 < 101:
                a = '상당히 나쁨'
            elif learn2 < 151:
                 a = '매우나쁨'
            elif learn2 > 150:
                 a = '최악'
            embed = discord.Embed(title=learn[1]+'초미세먼지',description='**'+str(learn2)+'㎍/㎥ \n'+a+'**\n'+div2.text+'\n'+'네이버 초미세먼지/초미세먼지 기준 미세미세8단계',color=0x00ff00)
            await app.edit_message(meg,embed=embed)	

  
	


	
     if message.content.startswith('_정보'):
           date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
           embed = discord.Embed(color=0x00ff00)
           embed.add_field(name="이름",value=message.author.name,inline=True)
           embed.add_field(name='서버닉네임',value=message.author.display_name, inline=True)
           embed.add_field(name='가입일',value=str(date.year) +'년' +str(date.month) + '월' + str(date.day) + '일', inline=True)
           embed.add_field(name='아이디',value=message.author.id,inline=True)
           embed.set_thumbnail(url=message.author.avatar_url)
           await app.send_message(channel,embed=embed)      
	
     if message.content.startswith("_프로필"):

        text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)

        vrsize = int(vrsize)

        for i in range(1, vrsize):
            text = text + " " + learn[i]
        for user in message.mentions:
            embed = discord.Embed(color=0xffffff)
            embed.set_image(url=user.avatar_url)
            await app.send_message(message.channel, embed=embed)  




     if message.content.startswith('공지'):
        if id in owner:
            notice = message.content.replace('공지', "")
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신 준비중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="Log", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/cb622728424ec6a039c3a5f6510359db.webp?size=1024")
            embed.set_footer(text="로그봇")
            mssg = await app.send_message(message.channel, embed=embed)
            a = []
            b = []
            e = []
            ec = {}
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="Log", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/cb622728424ec6a039c3a5f6510359db.webp?size=1024")
            embed.set_footer(text="로그봇")
            await app.edit_message(mssg, embed=embed)
            for server in app.servers:
                for channel in server.channels:
                    for tag in set.allowprefix:
                        if tag in channel.name:
                            dtat = True
                            for distag in set.disallowprefix:
                                if distag in channel.name:
                                    dtat = False
                            if dtat:
                                if not server.id in a:
                                    try:
                                        await app.send_message(channel, notice)
                                    except discord.HTTPException:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "HTTPException"
                                    except discord.Forbidden:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "Forbidden"
                                    except discord.NotFound:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "NotFound"
                                    except discord.InvalidArgument:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "InvalidArgument"
                                    else:
                                        a.append(str(server.id))
                                        b.append(str(channel.id))
            asdf = "```\n"
            for server in app.servers:
                if not server.id in a:
                    if set.nfct:
                        try:
                            ch = await app.create_channel(server, set.nfctname)
                            await app.send_message(ch, notice)
                        except:
                            asdf = asdf + str(server.name) + "[채널 생성 실패]\n"
                        else:
                            asdf = asdf + str(server.name) + "[채널 생성 및 재발송 성공]\n"
                    else:
                        asdf = asdf + str(server.name) + "\n"
            asdf = asdf + "```"
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신완료!", value="<@" + message.author.id + ">", inline=True)
            bs = "```\n"
            es = "```\n"
            for bf in b:
                bn = app.get_channel(bf).name
                bs = bs + str(bn) + "\n"
            for ef in e:
                en = app.get_channel(ef).name
                es = es + str(app.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
            bs = bs + "```"
            es = es + "```"
            if bs == "``````":
                bs = "``` ```"
            if es == "``````":
                es = "``` ```"
            if asdf == "``````":
                asdf = "``` ```"
            sucess = bs
            missing = es
            notfound = asdf
            embed.add_field(name="공지 발신 성공 채널:", value=sucess, inline=True)
            embed.add_field(name="공지 발신 실패 채널:", value=missing, inline=True)
            embed.add_field(name="공지 채널 없는 서버:", value=notfound, inline=True)
            embed.set_author(name="Log", icon_url="https://cdn.discordapp.com/avatars/480568196286644224/cb622728424ec6a039c3a5f6510359db.webp?size=1024")
            embed.set_footer(text="로그봇")
            await app.edit_message(mssg, embed=embed)
        else:
            await app.send_message(message.channel, "`공지기능오류`")           

            
      

            

access_token = os.environ["BOT_TOKEN"] 
app.run (access_token)
