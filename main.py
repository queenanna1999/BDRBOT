#Work with Python 3.9.1
import discord
import asyncio
import datetime
import logging
import random
import traceback
import time
import datetime
import os
import urllib
import bs4
import re
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

 
app = discord.Client()

@app.event
async def on_ready():
    print('로그인 중 입니다 ..!')                          
    print(app.user.name)                                   
    print(app.user.id)
    print('===============')
    game = discord.Game("!도와줘 = 명령어 모음")
    await app.change_presence(status=discord.Status.online, activity=game)
    
@app.event
async def on_member_join(member):
    fmt = '{1.name} 서버에 온 것을 진심으로 환영합니다 {0.mention} 님'    #신규유저한테만 보여지는 메세지 입니다.
    channel = member.server.get_channel("585087748952817665")
    await app.message.channel.send( fmt.format(member, member.server))
    await app.message.channel.send(member, "안녕? 난 뉴 배돌이야.")
    await app.message.channel.send(member, "뭐 궁금한 점이 있으면 나한테 물어봐.")
    await app.message.channel.send(member, "내가 알려줄 수 있는 범위 안에서 최선을 다해 알려줄테니까.")
    await app.message.channel.send(member, "아 참! 우리 서버에 들어온 것을 환영해~")
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("585087748952817665")         
    fmt = '{0.mention} 님이 서버를 떠나셨습니다'
    await app.message.channel.send( fmt.format(member, member.server))
          

@app.event
async def on_message(message):

    if message.content.startswith("!도와줘"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어 목록',
            description = '아래는 명령어 목록 입니다. 명령어 목록은 계속 업데이트 중 입니다.',
            colour = discord.Colour.red()
        )

        #embed.set_footer(text = '')
        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '!안녕', value = '배돌이가 인사를 해줍니다',inline = False)
        embed.add_field(name='!코로나', value='배돌이가 실시간 코로나 현황을 불러옵니다', inline=False)
        embed.add_field(name='!컴퓨터는?', value=' 배돌이가 믿음직한 컴퓨터 업체들을 선별해드립니다 (광고 X) ', inline=False)
        embed.add_field(name='!커뮤니티 웹사이트 추천', value=' 배돌이가 괜찮은 커뮤니티 사이트를 추천해줍니다 ', inline=False)
        embed.add_field(name='!볼 만한 유튜버 추천', value=' 배돌이가 괜찮은 유튜버를 추천해줍니다 ', inline=False)
        embed.add_field(name='!모바일 게임 추천', value=' 배돌이가 현재 흥행하는 모바일 게임을 추천해줍니다 (광고 X) ', inline=False)
        embed.add_field(name='!자기소개', value=' 배돌이가 자기소개를 해줍니다 ', inline=False)
        embed.add_field(name='!PC 게임 추천', value=' 배돌이가 현재 흥행하는 PC 게임을 추천해줍니다 ', inline=False)
        embed.add_field(name='!언어', value=' 배돌이가 무슨 언어를 기반으로 개발되어지고 있는지 알려줍니다 ', inline=False)
        embed.add_field(name='!오늘 내 생일이야', value=' 배돌이가 생일을 축하해줍니다 ', inline=False)
        embed.add_field(name='!랜덤주사위', value=' 배돌이가 랜덤으로 주사위를 굴려줍니다 ', inline=False)
        embed.add_field(name='!오늘뭐할까', value=' 배돌이에게 오늘 하루 할 일을 정해달라고 물어보세요! ', inline=False)
        embed.add_field(name='!오늘의상식', value=' 배돌이가 무작위로 알아두기만 해도 도움이 될만한 기본상식 하나를 알려줍니다 ', inline=False)
        embed.add_field(name='!볼 만한 영화 추천', value=' 배돌이가 제일 괜찮은 영화들을 한편 소개해줍니다 ', inline=False)
        embed.add_field(name='!패치노트', value=' 배돌이가 자신의 패치노트를 불러옵니다  ', inline=False)

        await message.channel.send(channel,embed=embed)
        
        

        
    if message.content.startswith("!안녕"):             #배돌이가 인사를 해줍니다.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)       
        msg = "{0.author.mention} 안녕?? 반가워, 그동안 잘 지냈니.".format(message)
        await message.channel.send( msg)
        
    
        
    if message.content.startswith("!컴퓨터는?"):              #근거있는 자료들만 모았습니다. 컴마왕 관련 자료들은 신뢰하셔도 괜찮습니다.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 4)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="혹시 너 it 관련 정보도 부족하고, 조립 및 A/S가 두렵니? 그렇다면, 컴퓨존을 추천해줄께", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="컴퓨존은 1991년 노인호 대표와 김태선 대표가 '태인시스템'이라는 회사를 설립하고 출발한 기점으로", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="1999년 '컴퓨존'으로 상호를 변경하고 아직까지 그 명성을 이어나가고 있는 컴퓨터 및 각종 전자기기 판매 업체야.", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="국내 컴퓨터 조립 업계 1위라고 불릴 만큼 국내 컴퓨터 판매 쇼핑몰 업계중에 규모가 가장 크고, 독보적인 지위를 차지하고 있지.", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="하지만 근무환경이나 A/S 등 여러 방면에서 전현직 직원들의 평은 대단히 좋지 않더라. 뭐 완벽한 회사는 없잖아..?", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="컴퓨터에 대한 정보가 부족한데, 컴퓨터는 사고 싶다고? 그러면 다나와를 추천해줄께.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="2000년부터 온라인 가격비교 서비스를 제공하는 대한민국의 사이트. (주)다나와에서 운영하고 있지.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="가장 많은 업체들이 참여한 규모의 경제를 이룬 상태이기 때문에 ", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="가격 비교가 실 구매시에 상당히 정확하며, 특히 현재 시장에서 인지도가 높은 상품들을 비교하기 좋아.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="전자제품, 특히 컴퓨터 부품을 기반으로 성장한 사이트이다보니 검색필터가 상당히 자세하고 정확하다는 장점이 매우 크지.", color=0x0000ff))
        
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="컴마왕은 추천하고 싶지가 않네...", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="단순히 컴퓨터에 대한 지식이 없고, 그냥 비싼게 최고라고 생각하면 여기서 알아보는게 정확하단다...", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="가서 주변 컴잘알들에게 물어보렴, 컴마왕 어떻게 생각하냐고.", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="참고로 듣보잡 업체들 특징이 뭔지 아니? 스트리머 및 유튜버들에게 광고를 부탁한다는 점이야. ", color=0xff0000))
            
    if message.content.startswith("!커뮤니티 웹사이트 추천"):       #추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 7)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="네이버 카페는 어떠니", color=0x0000ff))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="디시인사이드는 어때??", color=0x0000ff))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="인벤은 해볼 생각 없어?", color=0x0000ff))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="클리앙은 어떠니?", color=0x0000ff))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="오늘의유머는 해볼 생각 없어?", color=0x0000ff))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="겨울왕국 갤러리는 어떠니??", color=0x0000ff))            

    if message.content.startswith("!볼 만한 유튜버 추천"):             #다소 편협함. 추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 11)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드, 오버워치 스트리머 및 유튜버이신 군림보님은 어떠니", color=0xff0000))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="종합게임 스트리머 및 유튜버이신 김재원님은 괜찮지 않니?", color=0xff0000))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="IT 제품들을 리뷰 및 설명해주시는 잇섭님은 볼 생각 들지 않니?", color=0xff0000))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="보겸은 어떠니?", color=0xff0000))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드 스트리머 및 유튜버인 김블루는 어때?", color=0xff0000))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="하이톤의 목소리가 매력이신 배틀그라운드 스트리머 및 유튜버인 연다는??", color=0xff0000))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="항상 재밌는 카톡썰들을 보여주시는 오늘의카톡은??", color=0xff0000))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 명령어를 다시 입력하세요,,,", color=0xfefe00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="죄송해요,, 이해를 하지 못했어요, 다시 명령어를 입력해주시겠어요...?", color=0xfefe00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="영화 리뷰어이신 홍시네마님은?", color=0xff0000))
        
    if message.content.startswith("!모바일 게임 추천"):       #추가바람
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 7)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="클래시 오브 클랜은 어떠니?", color=0x0000ff))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드 모바일은 어때??", color=0x0000ff))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="펜타스톰은 해볼 생각 없어?", color=0x0000ff))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="마인크래프트 해보지 그래? ㅋㅋㅋ", color=0x0000ff))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="마블 퓨처 파이트 해봐, 추억의 게임이잖니", color=0x0000ff))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="콜 오브 듀티 모바일은 해볼 생각 없니?", color=0x0000ff))            
        
    if message.content.startswith("!자기소개"):        #이 부분은 이 소스를 수정해서 새로운 자작봇을 만드실 분들에 해당하시는 분들만 수정 부탁드립니다.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 안녕, 난 뉴 배돌이야.  ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 너희들이 디스코드 서버를 잘 이용할 수 있도록  ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 도와주는 디스코드 서버 한정 어시스턴트야. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 내 이름의 뜻은 ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" [제 2의 배돌이 프로젝트] 의 줄인말이야 ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" [ (제 2의) 배돌이 프로젝트] 는 전세계 배틀그라운드, 배틀그라운드 모바일 유저들을 위한 프로젝트 였지, 지금은 아니지만. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        msg = "널 또 보길 바랄께, 나중에 보자. {0.author.mention} ".format(message)
        await message.channel.send( msg)
        
    if message.content.startswith("!PC 게임 추천"):      #다소 편협함. 추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 12)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드는 어떠니", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="오버워치는 어때??", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="리그 오브 레전드는 해볼 생각 없어?", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="월드 오브 탱크는?", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="히어로즈 오브 더 스톰은 해볼 생각 없어?", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="서든어택은???", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="마인크래프트는 어떠니?", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="피파 온라인 4는 꽤 재밌어보이던데.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="GTA5도 한번 시작해봐, 꽤 재밌어.", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="리니지 한번 시작해봐.", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="카운터스트라이크 온라인도 한번 해보면 재밌을 거야.", color=0x00ff00))           

    if message.content.startswith("!패치노트"):                #배돌이의 패치노트입니다. 패치 하나 할때마다 업데이트 됩니다.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="*2018년 12월 ", description=" 배돌이 프로젝트 구상 및 개발 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="*2019년 06월 01일 ", description=" 갑작스런 사태로 컴퓨터에 저장해놓은 프로젝트 파일이 사라짐. ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="*2019년 06월 02일 ", description=" 배돌이 프로젝트 기반의 뉴 배돌이 베타 0.0.1을 개발 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.2  ", description=" 명령어 목록 작성, 일부 에러 구문 수정! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.3 ", description=" 일부 에러 구문 수정, 일부 명령어 추가! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.4 ", description=" 2019년 06월 27일 목요일, 배돌이봇 호스팅 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.5 ", description=" 2019년 06월 29일 토요일, 배돌이 명령어 목록 Ui 일부 수정 및 업데이트! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.6 ", description=" 2019년 06월 29일 토요일, 일부 Ui 수정!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.7 ", description=" 2019년 06월 30일 일요일, 생일 축하 기능과 랜덤주사위 기능 업데이트!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.8 ", description=" 2019년 07월 05일 금요일, 이제 배돌이에게 조언을 받아보실 수 있습니다. 지금 당장 체험해보세요.", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.9 ", description=" 2019년 07월 05일 금요일, 일부 Ui 수정!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.0 ", description=" 2019년 07월 05일 금요일, 배돌이 공지 기능 업데이트", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.1 ", description=" 2019년 07월 27일 토요일, 배돌이 공지 기능 삭제, 대신 !오늘의상식 기능으로 대체합니다. ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.2 ", description=" 2019년 07월 28일 일요일, 배돌이가 영화 한편을 무작위로 추천해줄수 있습니다, 지금 당장 추천받아보세요! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.3 ", description=" 2019년 07월 28일 일요일, 배돌이가 오늘의운세를 알려줍니다. 지금 당장 운세를 무료로 받아보세요!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.4 ", description=" 2019년 08월 09일 금요일, 배돌이가 네이버 기반인 현 실시간 검색어 랭킹을 알려줍니다!(2019년08월21일 다시 부활한 기능입니다.)", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.5 ", description=" 2019년 08월 10일 토요일, 배돌이가 이제 커여운 이모티콘을 사용할 수 있습니다.", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.6 ", description=" 2019년 08월 22일 목요일, 배돌이가 다음 검색 엔진 기반인 현재 영화 랭킹을 알려줍니다.", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *1.0.0 ", description=" 2020년 12월 27일 일요일, 배돌이가 드디어 1.0으로 업그레이드 되었습니다.", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ", description=" ***패치노트는 계속 업데이트 할 예정입니다 ^00^ ", color=0x00fefe)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!오늘의상식"): 
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        #아이디어 추가바람. 
        await message.channel.send(embed=discord.Embed(title="안녕? 다음 정보들은 알아두기만 해도 좋은 기본상식들이야.", color=0xfefefe))
        randomNum = random.randrange(1, 4)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="차가운 물은 뜨거운 물보다 더 빨리 데워지고, 뜨거운 물은 차가운 물보다 더 빨리 얼려진다..", color=0xffaaaa))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="마블 코믹스의 토니 스타크의 영어 풀네임은 Anthony Edward Stark 이다.", color=0xffaaaa))
            await message.channel.send(embed=discord.Embed(title="해외에서는 알고있는 사람들이 많았으나 한국에서는 Tony stark로만 알고 있는 사람들이 많다.", color=0xffaaaa))
            await message.channel.send(embed=discord.Embed(title="이유는 한국에서는 원작보다 영화가 제일 인기가 많았기 때문이라고 한다...", color=0xffaaaa))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="집에 있는 변기가 막혔을 때는 페트병의 50퍼센트를 정확히 자른 후 받침대가 있는 부분으로 뚜러뻥을 대체 할 수 있다.", color=0xffaaaa))


    if message.content.startswith("!볼 만한 영화 추천"):           #다소 편협함. 추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)       
        await message.channel.send(embed=discord.Embed(title="안녕? 난 니가 어떤 애인진 모르지만, 정성껏 최선을 다해 추천해줄게.", color=0xfefefe))
        randomNum = random.randrange(1, 12)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="오늘같은 날에는 추억을 되돌아보게 해줄만한 [해리포터 시리즈] 는 어떠니?", color=0xfefe00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="어벤져스 인피니티 워는 어때?", color=0xfefe00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="엑스맨 데이즈 오브 퓨쳐 패스트는?", color=0xfefe00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="인터스텔라는 어떠니? ", color=0xfefe00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="토비 맥과이어가 주연인 [스파이더맨 시리즈]는??", color=0xfefe00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="가끔은 로맨스 영화도 재밌게 느껴지는데.. 노트북은 어떠니?", color=0xfefe00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="파라노말 액티비티 시리즈는 어떠니? 오늘 같은 날에 최고의 조합인 것 같은데.", color=0xfefe00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="캡틴아메리카 윈터솔저 어떠니? 그나마 MCU작품들 중에서 제일 극찬 받았던 히어로물 작품인데..", color=0xfefe00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="가끔은 [ 터미네이터 시리즈 ]도 재밌어, 이 시리즈는 어떠니?", color=0xfefe00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="[ 트랜스포머 시리즈 ]는 어떠니?", color=0xfefe00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 관리자에게 연락바랍니다...", color=0xff0000))
        




            
            

         
    if message.content.startswith("!언어"):            #이 소스를 참고해서 새로운 자작봇을 만드실 분들에 해당하시는 분들만 수정 부탁드립니다.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        embed = discord.Embed(title="안녕? 난 뉴 배돌이야. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="지금부터 내가 무슨 언어를 기반으로 개발되어지고 있는지 알려줄께. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 우선 나는 PYTHON3으로 개발되고 있어. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 기본적인 기능들을 구현하기에는 적합한 언어지. 우선 내 개발자는 전문가가 아니거든.", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" PYTHON 은 1991년 프로그래머인 귀도 반 로섬(Guido van Rossum)이 발표한 고급 프로그래밍 언어로, ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed) 
        embed = discord.Embed(title=" 플랫폼 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어로 많이 알려져 있어.", description=" ", color=0xaaaaff)                      
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 특히, 파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python's Flying Circus〉에서 따온 것이야.", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 재미있는 사실은 1989년 크리스마스 주에, 연구실이 닫혀있어서 그저 심심해서 만든 작품이 파이썬이라는게 .. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
      
    if message.content.startswith('!오늘 내 생일이야'):          #없애도 되는 기능. 사실 별 쓸모없는 기능.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        msg = "{0.author.mention} 생일 축하해 !!".format(message) #그냥 자축 기능. 개발자가 외로운 솔로라 만들어본 기능.
        await message.channel.send( msg)
        
    if message.content.startswith("!랜덤주사위"):         #이것도 없어도 지장없는 기능. 
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 7) 
        print(randomNum)
        if randomNum == 1:
            await message.channel.send( embed=discord.Embed(description=':game_die: '+ ':one:',color=0xfefe00))
        if randomNum == 2:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':two:',color=0xfefe00))
        if randomNum ==3:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':three:',color=0xfefe00))
        if randomNum ==4:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':four:',color=0xfefe00))
        if randomNum ==5:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':five:',color=0xfefe00))
        if randomNum ==6:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':six: ',color=0xfefe00))
        
    if message.content.startswith('!오늘뭐할까'):           #추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 16)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="그냥 아무것도 하지않는게 더 났지 않을까?", color=0xfe00fe))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="그냥 잠이나 충분히 자는게 더 나을듯 해", color=0xfe00fe))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="공부하는 것도 나쁘지 않을거야", color=0xfe00fe))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="영화 한편보는 건 어때?", color=0xfe00fe))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="신책하는 것도 나쁘지 않을텐데, 가벼운 산책은 머리를 맑게 해줘.", color=0xfe00fe))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="미쳤니? 이 날씨에?! 그냥 집에서 게임이나 하는게 현명한 선택이야.", color=0xfe00fe))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="부모님한테 효도라도 해볼 생각은 없니? 안마라도 해드려.", color=0xfe00fe))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="하나님한테 기도드려봐. 해결될거야.", color=0xfe00fe))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="정말 한가하다.. 너 시간 많나보다? 기억해. 너는 한낱 인간이고, 삶은 영원하지 않다고.", color=0xfe00fe))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="솔직히 말해봐. 너 지금 모태솔로지?", color=0xfe00fe))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="문화생활이라도 즐겨봐. 너 그러다 병나. 여기다 물어볼 정도면 넌 심각해", color=0xfe00fe))
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="넌 좋아하는 취미가 뭐니? 좋아하는 취미를 즐기면서 지금 이 시간을 즐겨.", color=0xfe00fe))
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="너 정말 모태솔로 아닌거 확실해? 커플들은 보통 여기서 물어보지 않는단다;;", color=0xfe00fe))
        if randomNum==14:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 치명적인 오류 발생!! 다시 명령어를 입력하세요...", color=0xff0000))
        if randomNum==15:
            await message.channel.send(embed=discord.Embed(title="헬스장이라도 가봐. 건강은 자기자신이 챙기는거다.?!", color=0xfe00fe))
            
    if message.content.startswith("!오늘의운세"):       #추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        await message.channel.send(embed=discord.Embed(title="니가 받은 숫자를 [!숫자]와 동일한 방식으로 채팅에다 다시 적어주렴.", color=0xfefefe))
        randomNum = random.randrange(1, 12)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="10", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="5", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="4", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="3", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="2", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="1", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="9", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="7", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="8", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="6", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 관리자에게 연락하세요...", color=0xff0000))
            
    if message.content.startswith("!3"):
        await message.channel.send("당신의 행운의 숫자는 3 입니다. ")
        await message.channel.send("행운의 색 - 흰색 ")
        await message.channel.send("행운의 아이템 및 장소 - 부드러운 소재의 블라우스 또는 스커트. 진주, 다이아, 물가, 공원 ")
        await message.channel.send("명심해 둘 것 - 용서하기 ")
        await message.channel.send("당신은 주위 사람들을 꼼꼼하게 챙기고, 섬세하기 때문에 꽤 인기가 많은 타입입니다.  ")
        await message.channel.send("하지만 속마음이 정열적이라 자신을 좋아해 주도록 상대방에게 강요하는 경향을 가지고 있기도 합니다. ")
        await message.channel.send("때문에 당신은 상대방의 반응에 매우 민감하며 그로 인해 유난히 많은 상처를 받기도 합니다.  ")
        await message.channel.send("하지만, 앞으로는 상대방이 당신이 원하는 만큼을 주지 않는다고해서 실망하지 말고, 너그러운 마음으로 관계를 지속해보세요. ")
        await message.channel.send("당신이 강요하지 않아도 당신의 장점으로 상대방을 끌어당길 수 있습니다.  ")
        await message.channel.send("그 점을 잊지 마시고, 상대에게 좀 더 편안하게 대해 보시기 바랍니다.  ")
        await message.channel.send("그렇게 하면 당신은 상대를 편하게 한다는 매력을 하나 더 추가하게 되고, 사랑에 성공할 수 있을 것입니다.  ")
        await message.channel.send("============ ")
        await message.channel.send("모든 일은 억지로 하려고 해서 되는 것이 아닐 때가 많습니다.  ")
        await message.channel.send("특히나 사람의 마음은 더욱 그렇겠지요. 억지로 내것을 만들려고 하면 할수록 멀어져 갈 수 있습니다.  ")
        await message.channel.send("당신만을 생각하기 보다는 좀 더 상대를 배려해주세요. 그리고 사소한 잘못은 용서해 주는 것이 포인트이니 이 점을 명심하십시오.  ")
        await message.channel.send("그리하면 훗날 당신에게 더 좋은 운이 돌아올 것입니다.  ")
        
    if message.content.startswith("!7"):
        await message.channel.send("당신의 행운의 숫자는 7 입니다. ")
        await message.channel.send("행운의 색 - 금색")
        await message.channel.send("행운의 아이템 및 장소 - 잘 빠진 정장, 오팔, 오닉스, 캐치아이, 은행 ")
        await message.channel.send("명심해 둘 것 - 행동하라 ")
        await message.channel.send("당신은 다소 내향적이며, 침착함과 인내력을 지닌 타입입니다. 또한 성실하고 조용한 성격덕분에 남들에게 신뢰를 얻기 쉽습니다.   ")
        await message.channel.send("모든 일을 결정할 때 침착하게 차근차근 앞뒤를 따져서 선택을 하기 때문에 그러한 모습이 보는 이로 하여금 당신의 결정에 믿음을 주는 편입니다. ")
        await message.channel.send("또 항상 묵묵하게 자신의 자리를 잘 지키는 타입이기도 합니다.  ")
        await message.channel.send("그러나 실제로는 매우 승부욕이 강해, 겉으로 내색하지 않지만 남에게 지기 싫어하는 성격도 가지고 있습니다.")
        await message.channel.send("이것은 늘 부족한 행동력으로 인해 실행에 옮기지 못하기도 하니 그 점이 당신의 가장 큰 단점이라고 할 수 있겠습니다.  ")
        await message.channel.send("그 점을 잊지 마시고, 상대에게 좀 더 편안하게 대해 보시기 바랍니다.  ")
        await message.channel.send("아무리 신중하고 잘된 결정이라고 할지라도 그것을 실행에 옮기지 않는다면 그 결정은 무의미할 뿐입니다.  ")
        await message.channel.send("============ ")
        await message.channel.send("그러니 여러모로 확실한 성격을 가진 당신은, 앞으로 과감한 행동력만 가미한다면 당신의 신중한 결정과   ")
        await message.channel.send("더불어 많은 이득을 얻을 수도 있다는 것을 명심하고 모든 상황에 자신감있게, 추진력있게 대응하십시오. ")
        
      
    if message.content.startswith("!8"):
        await message.channel.send("당신의 행운의 숫자는 8 입니다. ")
        await message.channel.send("행운의 색 - 빨간색")
        await message.channel.send("행운의 아이템 및 장소 - 보송보송하고 얇은 소재의 니트, 인조모피, 루비, 가닛(석류석), 출생지 ")
        await message.channel.send("명심해 둘 것 - 정리하기 ")
        await message.channel.send("당신은 감수성이 풍부하고 정이 많기 때문에 좋아하는 사람에게는 진심을 다해 소중히 대하는 타입입니다.    ")
        await message.channel.send("또한 당신의 그런 성격이 사람들과의 끈끈한 관계를 만들어 줄 수 있습니다. ")
        await message.channel.send("상대에 대한 배려를 아끼지 않는 모습에 주변 사람들이 당신의 곁에 오래 머물고 싶어하는 등  ")
        await message.channel.send("매우 긴밀한 인간관계를 맺게 됩니다.")
        await message.channel.send("그러나 절친한 사람에게는 애교도 잘 떨고 귀여운 모습을 보여주기도 하는 반면, 마음이 잘 맞지 않은 사람과는 상대도 하기 싫어하는 극단적인 성격을 가지고 있기도 합니다.  ")
        await message.channel.send("그래서 당신의 태도에 따라 당신에 대한 평가는 상반될 수 있습니다.  ")
        await message.channel.send("하지만, 원활한 사회생활을 위해서는 마음이 맞지 않는 사람들에게도 조금은 열린 마음으로 배려해주는 태도가 필요할 것입니다.   ")
        await message.channel.send("============ ")
        await message.channel.send("사람은 누구든 원하는 것만 하고 살 수는 없는 법! 사회생활 혹은 단체생활을 하다보면 싫은 사람과도 마주쳐야 할 상황이 있음을 명심하고   ")
        await message.channel.send("상대방에게 나쁜 인상을 준다는 것은 늘 당신에게 분리한 조건으로 작용하는 경우가 많다는 것을 명심하고,  ")
        await message.channel.send("싫어도 내색하지 않을 수 있는 인내심을 기르십시오.  ")
        
        
    if message.content.startswith("!9"):
        await message.channel.send("당신의 행운의 숫자는 9 입니다. ")
        await message.channel.send("행운의 색 - 보라색")
        await message.channel.send("행운의 아이템 및 장소 - 모자, 깔끔하게 정리한 머리, 자수정, 청금속, 서점, 도서관")
        await message.channel.send("명심해 둘 것 - 포기 ")
        await message.channel.send("당신은 선천적으로 두뇌 회전이 매우 빠르고 총명합니다. 때문에 모든 면에서 계산이 빠르고 그로 인한 행동력도 좋은 편입니다.")
        await message.channel.send("또한, 수다 떨기를 좋아하며 천진난만해 보이는 면이 있는데, 그것이 사람들로 하여금 호감을 불러일으키는 요인이 됩니다. ")
        await message.channel.send("그래서 당신은 사람들 사이에서 재미있는 캐릭터로 느껴질 수 있기에 항상 주변에 사람이 많을 것이며, 인기인으로 불리기도 합니다.")
        await message.channel.send("하지만, 수다가 지나치면 마이너스 요인으로 작용하므로 주의하세요. 모든 실수는 입에서 나온다고, ")
        await message.channel.send("말이 많아지다 보면 분명 당신도 모르게 실수를 하게 될 경우 또한 많아지게 될 것입니다. ")
        await message.channel.send("그러므로 늘 언행을 단정히 하는 것이 좋습니다. ")
        await message.channel.send("그리고, 말이 많아져 당신도 모르는 사이에 당신의 비밀을 털어놓게 될 소지가 있는데, 이 점을 주의하여야 할 것입니다. ")
        await message.channel.send("============ ")
        await message.channel.send("솔직한 것도 좋지만, 가끔은 개성있는 당신의 모습이 사람들에게 조금은 신비감을 느끼도록 하는 것이 당신 주변의 사람들을 쉽게 질리지 않게 하는 방법 임을 잊지 마십시오.")

        
    if message.content.startswith("!10"):
        await message.channel.send("당신의 행운의 숫자는 10 입니다. ")
        await message.channel.send("행운의 색 - 은색")
        await message.channel.send("행운의 아이템 및 장소 - 실크소재의 옷, 다이아, 메이브 펄(진주색), 속도감을 느낄 수 있는 곳")
        await message.channel.send("명심해 둘 것 - 인내할것 ")
        await message.channel.send("당신은 모든 일에 호기심이 왕성하고 다양한 사람들과 쉽게 친해지는 타입입니다. 때문에 왕성한 호기심으로 여러 가지 다양한 분야에 관심을 가지게 되고 ")
        await message.channel.send("그로 인해 수많은 인간관계를 형성하게 되는 것입니다. 또한, 사교적이고 솔직한 타입이기 때문에 주변에 항상 사람이 많을 것입니다.")
        await message.channel.send("하지만, 다소 실증을 잘 내며 교제상대가 수시로 바뀌기 때문에 깊은 관계를 유지하기 힘든 면도 있으니 이 점을 주의하세요.")
        await message.channel.send("인간관계에서 실증을 잘 낸다는 것은 매우 좋지 않은 부분입니다. ")
        await message.channel.send("다양한 관계를 형성하는 만큼 깊이가 없다면 정작 당신이 힘들거나 도움이 필요한 순간에 당신이 속을 터놓고 고민을 말 하거나")
        await message.channel.send("혹은 도움을 요청할 만한 사람이 없다는 것을 의미하기도 합니다. ")
        await message.channel.send("때문에 항상 대인관계에 있어서 인내하고 배려하는 태도가 필요하다는 것을 잊지 마시고 모든 인간관계에 신중을 기하도록 하심이 좋습니다.")
        
        
    if message.content.startswith("!1"):
        await message.channel.send("당신의 행운의 숫자는 1 입니다. ")
        await message.channel.send("행운의 색 - 파란색")
        await message.channel.send("행운의 아이템 및 장소 - 파란색 계통의 포인트가 들어간 코디, 청바지, 사파이어, 아쿠아마린, 바다, 섬, 강 ")
        await message.channel.send("명심해 둘 것 - 봉사한다 ")
        await message.channel.send("당신은 매우 너그러운 성격이며, 주위 사람들이 잘 따르는 성향을 지니고 있습니다. 때문에 당신 주변에는 당신의 리드를 받고자 하는 사람이 많을 것입니다. ")
        await message.channel.send("그리고 그들을 그들의 바람대로 잘 이끌어 주는 리더십이 당신의 매력으로 작용하기도 합니다. ")
        await message.channel.send("당신의 자신감 있는 태도가 주위 사람들에게 믿음을 주기 때문에 따르는 사람이 많은 것은 어쩌면 당연한 일이기도 합니다.")
        await message.channel.send("하지만, 지나치게 리더십을 강조하면 반발심을 사게 될 수 있으니 조심하시는 것이 좋습니다. ")
        await message.channel.send("당신을 따르는 이가 많다는 것은 당신이 그만큼 그들을 배려하면서 잘 이끌어줬기 때문이지 그들이 무조건 당신을 위해 따르는 것은 아닙니다. ")
        await message.channel.send("무조건적인 리드는 거부감을 일으킬 수 있음을 명심하십시오. 가끔은 뒤에서 따라주는 사람들을 먼저 생각해주는 배려심이 필요합니다. ")
        await message.channel.send("리드를 위한 리드가 아니라 배려와 믿음을 동반한 리드여야 당신의 매력이 빛을 발할 것이며, ")
        await message.channel.send("============ ")
        await message.channel.send("그들의 당신에 생각도 변하지 않을 것이니 기억하시고 늘 보살피는 태도를 유지하십시오. ")
        
        
    if message.content.startswith("!2"):
        await message.channel.send("당신의 행운의 숫자는 2 입니다. ")
        await message.channel.send("행운의 색 - 검정색")
        await message.channel.send("행운의 아이템 및 장소 - 롱코트나 가디건, 오닉스, 검은 돌, 빌딩, 도시")
        await message.channel.send("명심해 둘 것 - 냉혹해 질 것 ")
        await message.channel.send("당신은 주위 사람들과 스스럼없이 지낼 수 있는 재능을 가진 사람으로 주위 사람들도 당신을 좋아해 늘 좋은 인간관계를 유지하고 있습니다.")
        await message.channel.send("이런 당신의 좋은 성격이 주변에 많은 사람들과 화합할 수 있게 만들어줄 것이며 늘 주변 사람들에게 당신은 성격 좋은 사람으로 인식될 것입니다.")
        await message.channel.send("하지만, 항상 좋은 사람처럼 보이고 싶어하기 때문에 정작 당신의 본심을 잘 표현하지 못하고 속으로 삭혀 혼자 힘들어 할 때가 있네요. ")
        await message.channel.send("상대를 배려하는 것은 지극히 좋은 성격이지만, 이런 상황이 계속되면 우유부단한 사람처럼 보이기도 하니 ")
        await message.channel.send("적절한 의사표현을 할 수 있도록 노력하시는 것이 좋습니다.")
        await message.channel.send("뿐만 아니라 속으로 삭히다 보면 언젠가는 당신 자신도 지칠 수 있습니다. 그리고 당신이 주변 사람들로부터 위로받고 싶고, 대우 받고 싶을 때에도 그렇지 못할 수 있습니다.")
        await message.channel.send("대인관계에서 자신을 너무 드러내지 않거나 혹은 낮추는 것이 좋은 것만은 아니라는 사실을 깨닫고 ")
        await message.channel.send("============ ")
        await message.channel.send("사람들 앞에서 좀 더 솔직하게 자신의 모습을 드러내 보십시오.")
        
        
    if message.content.startswith("!4"):
        await message.channel.send("당신의 행운의 숫자는 4 입니다. ")
        await message.channel.send("행운의 색 - 초록색")
        await message.channel.send("행운의 아이템 및 장소 - 바지(팬츠)스타일, 에메랄드, 양산, 틀루마린, 나무, 산, 숲, 호수")
        await message.channel.send("명심해 둘 것 - 끝을 볼 수 있도록 결말을 지을 것")
        await message.channel.send("당신은 많은 사람들과 함께 있는 것을 좋아하는 타입입니다. 또한, 유난히 감수성이 풍부하여, 어딜 가나 인기가 많습니다. ")
        await message.channel.send("부드럽고 온화한 당신의 성격은 사람들에게 유한 사람으로 인식될 수 있게 할 것입니다.")
        await message.channel.send("하지만, 우유부단한 면이 있어 때로는 남에게 너무 의지하려하고, 입장이 난처한 상황에 처하면 그 자리를 회피하려고 하는 타입이기 때문에")
        await message.channel.send("일의 결말이 흐지부지하게 끝나버리는 경우가 있습니다.")
        await message.channel.send("이것은 당신의 단점 중에 하나라고 할 수 있는데, 이러한 모습은 다른 사람들에게 당신의 이미지를 안 좋게 보이게 할 것입니다. ")
        await message.channel.send("뿐만 아니라 만약 이런 상황이 반복될 경우에는 사람들이 당신에게서 조금씩 멀어질 수도 있습니다. ")
        await message.channel.send("그러니 조금은 결단력이 있는 모습을 보여주는 것이 좋겠습니다.")
        await message.channel.send("============ ")
        await message.channel.send("온화한 성격도 좋지만, 뭔가 맺고 끊음이 분명하고 정확하게 결말을 내는 것이 ")
        await message.channel.send("자신의 의지를 뚜렷하게 표출하는 의미이기도 하니 앞으로는 조금씩 이렇게 할 수 있도록 노력하십시오.")
        await message.channel.send("늘 성격좋고 뭐든 다 받아주는 사람, 가끔은 남에게 얕보일 소지가 있기도 하다는 것을 잊지 마시고")
        await message.channel.send("그럴 근원이 되는 일은 아예 만들지 않는 것이 좋습니다.")
        
    if message.content.startswith("!5"):
        await message.channel.send("당신의 행운의 숫자는 5 입니다. ")
        await message.channel.send("행운의 색 - 노란색")
        await message.channel.send("행운의 아이템 및 장소 - 금으로 된 액세서리, 토파즈, 옐로우 사파이어, 술집, BAR ")
        await message.channel.send("명심해 둘 것 - 서두르지 말 것, 성질을 급하게 부리지 말 것 ")
        await message.channel.send("당신은 본래 천성이 연예인과 같은 카리스마가 느껴지는 스타일이라 모든 사람들에게 동경의 대상이 될 뿐만 아니라 인기가 많아 항상 많은 이들의 관심을 한몸에 받습니다.")
        await message.channel.send("또한, 인간관계도 자연스럽게 형성되는 타입이기 때문에 주변에 많은 사람들이 있어서 혼자 있는 시간이 거의 없을 정도입니다. ")
        await message.channel.send("그러나 항상 많은 사람들의 동경을 받았기 때문에 타인의 대한 배려심이 부족합니다.  ")
        await message.channel.send("주변 사람들이 늘 당신을 중심으로 당신의 의견에 동조하고 맞춰준다고 하여 무조건 모든 일에 당신 마음대로 하려 든다면 그들은 더이상 당신을 동경하지 않을 것입니다.")
        await message.channel.send("때문에 거만한 태도는 금물이며, 매사에 자기중심적인 행동을 하지 않도록 주의하셔야 합니다.")
        await message.channel.send("항상 자신을 낮추고 겸손한 태도를 유지한다면 당신은 카리스마 있는 매력과 더불어 인간성도 좋은 사람으로 보일 것입니다.")
        await message.channel.send("그러니 자기 멋대로 행동하다가 주변의 사람들이 떨어져나가지 않도록 주의하시는 것이 바람직한 인간관계를 유지하는데에 도움을 준다는 것을 명심하십시오. ")
        await message.channel.send("============ ")
        await message.channel.send("매사 주변 사람들을 먼저 배려하는 생활태도는 늘 그들을 당신의 편이 되게 하여 줄 것입니다.")
        
        
    if message.content.startswith("!6"):
        await message.channel.send("당신의 행운의 숫자는 6 입니다. ")
        await message.channel.send("행운의 색 - 은색")
        await message.channel.send("행운의 아이템 및 장소 - 실크소재의 옷, 다이아, 메이브 펄(진주색), 속도감을 느낄 수 있는 곳")
        await message.channel.send("명심해 둘 것 - 인내할것 ")
        await message.channel.send("당신은 모든 일에 호기심이 왕성하고 다양한 사람들과 쉽게 친해지는 타입입니다. 때문에 왕성한 호기심으로 여러 가지 다양한 분야에 관심을 가지게 되고 ")
        await message.channel.send("그로 인해 수많은 인간관계를 형성하게 되는 것입니다. 또한, 사교적이고 솔직한 타입이기 때문에 주변에 항상 사람이 많을 것입니다.")
        await message.channel.send("하지만, 다소 실증을 잘 내며 교제상대가 수시로 바뀌기 때문에 깊은 관계를 유지하기 힘든 면도 있으니 이 점을 주의하세요.")
        await message.channel.send("인간관계에서 실증을 잘 낸다는 것은 매우 좋지 않은 부분입니다. ")
        await message.channel.send("다양한 관계를 형성하는 만큼 깊이가 없다면 정작 당신이 힘들거나 도움이 필요한 순간에 당신이 속을 터놓고 고민을 말 하거나")
        await message.channel.send("혹은 도움을 요청할 만한 사람이 없다는 것을 의미하기도 합니다. ")
        await message.channel.send("때문에 항상 대인관계에 있어서 인내하고 배려하는 태도가 필요하다는 것을 잊지 마시고 모든 인간관계에 신중을 기하도록 하심이 좋습니다.")

        
    if message.content.startswith("!이모티콘"):     #없어도 되는 기능.

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xffaaaa))  
        
    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):       
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)
    
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')
    
    
        embed = discord.Embed(
        title='네이버 급상승 검색어',
        description='검색어',
        color=discord.Color.green()
            )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False) 
            
        await message.channel.send(embed=embed)
        
        
    if message.content.startswith('!실시간영화랭킹') or message.content.startswith('!실영'):
        
        i1 = 0 
        embed = discord.Embed(
            title = "실시간 영화 랭킹",
            description = "",
            color= discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) 
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip() 
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd') 
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip() 
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  
            print(moviechartLi1Yerating)  
            print()
            embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) 


        await message.channel.send(embed=embed)
        
        

 
    if message.content.startswith("!코로나"):
        # 보건복지부 코로나 바이러스 정보사이트"
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        #주요 브리핑 및 뉴스링크
        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        # 통계수치
        statNum = []
        # 전일대비 수치
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="Covid-19 Virus Korea Status", description="",color=0x5CD1E5)
        embed.add_field(name="Data source : Ministry of Health and Welfare of Korea", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="Latest data refred time",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +" 자료입니다.", inline=False)
        embed.add_field(name="확진환자(누적)", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="완치환자(격리해제)", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="치료중(격리 중)", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name="- 최신 브리핑 1 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name="- 최신 브리핑 2 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        embed.set_footer(text='#사회적 거리두기 #Stay at Home')
        await message.channel.send("Covid-19 Virus Korea Status", embed=embed)   


    if message.content.startswith("닥쳐"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("시발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("니애미"):
        await message.channel.send("응 니애미 창녀")

    if message.content.startswith("ㄴㅇㅁ"):
        await message.channel.send("응 느그애미")

    if message.content.startswith("니애비"):
        await message.channel.send("응 니애비 외노자 ")

    if message.content.startswith("ㄴㅇㅂ"):
        await message.channel.send("응 느그애비 ")

    if message.content.startswith("개새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("닭쳐"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개샛기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("문재인"):
        await message.channel.send("욕 하지마라 진짜 뒤진다 ")

    if message.content.startswith("전라도"):
        await message.channel.send("지역 비하하지 마라 ")

    if message.content.startswith("ㅗ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅆㅂ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㄱㅅㄲ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개자식"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅋㅋㅋ"):
        await message.channel.send("쪼개지마라  ")

    if message.content.startswith("ㅇㅈㄹ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("이지랄"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("추미애"):
        await message.channel.send(" 진짜 욕하지 마라 ")

    if message.content.startswith("박원순"):
        await message.channel.send("패드립보다 심한 욕을 박네 니네 엄마가 그리 가르쳤냐 ")

    if message.content.startswith("대깨문"):
        await message.channel.send("와.. 이건 좀 심했다... 상처 받음.. ")

    if message.content.startswith("문빠"):
        await message.channel.send("와.. 이건 좀 심했다... 상처 받음.. ")

    if message.content.startswith("씹새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("10새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("십새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("십새기"):
        await message.channel.send("욕하지 마라")

    if message.content.startswith("씹새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("10새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개독"):
        await message.channel.send("종교 비하 발언 하지 마라 진짜 추방당하기 싫으면 ")

    if message.content.startswith("ㅁㄹ"):
        await message.channel.send("좆까 ")
      
    if message.content.startswith("좆까"):
        await message.channel.send("욕 작작해 시발련아 ")

    if message.content.startswith("ㅈㄲ"):
        await message.channel.send("하시발 추방 마렵다 ")

    if message.content.startswith("좃까"):
        await message.channel.send("진짜 뒤지기 전에 작작해라 ")

    if message.content.startswith("조까"):
        await message.channel.send("욕 작작 하렴^^ ")

    if message.content.startswith("조카"):
        await message.channel.send("욕 하지 마라 ")

    if message.content.startswith("좃카"):
        await message.channel.send("욕 하지 마라 ")

    if message.content.startswith("도리야"):
        await message.channel.send("넌 그분 이름을 언급할 자격이 없어 ")

    if message.content.startswith("도리도리곰도리"):
        await message.channel.send("넌 그분 이름을 언급할 자격이 없어 ")

    if message.content.startswith("삼성"):
        await message.channel.send("대한민국을 먹여살리는 국내 1위 기업 [킹!성!전!자] ")

    if message.content.startswith("애플"):
        await message.channel.send("대한민국을 병들게 하는 미국 기업 [애플=좆플] ")

    if message.content.startswith("아이폰"):
        await message.channel.send("대가리 없는 저능아들이나 환장하는 쓰레기 기업이 만든 쓰레기 폰 ")

    if message.content.startswith("갤럭시"):
        await message.channel.send("이 시대 최고의 엘리트들이 선호하는 대한민국 1위 기업 삼성의 스마트폰  ")

    if message.content.startswith("앱등이"):
        await message.channel.send("엄마없는새끼 ")

    if message.content.startswith("삼엽충"):
        await message.channel.send("이 시대 최고의 엘리트 ")

    if message.content.startswith("애플빠"):
        await message.channel.send("엄마없는새끼 ")

    if message.content.startswith("삼성빠"):
        await message.channel.send("이 시대 최고의 엘리트이자 천재이며 인싸 ")

    if message.content.startswith("개씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씹"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개좆"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씹할"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개지랄"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개족새"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("아다"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("동정"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("걸레"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("간나새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개새"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개돼지"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개나리"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개쓰레기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("고자"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("거지"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("졸라"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("존나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("좆나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("좃나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅈㄴ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("김치녀"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("꺼저"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("꺼져"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("급식"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("급식충"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개초딩"):
        await message.channel.send("욕하지 마라 ")   
      
      
    if message.content.startswith("ㅋㅋㅋ"):     #없어도 되는 기능.

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))
        
        
        
accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
