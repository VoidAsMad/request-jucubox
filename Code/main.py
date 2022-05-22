import discord
from discord.ext import commands
import asyncio
import random

from replit import db

bot = commands.Bot(command_prefix=['?'], intents=discord.Intents.all())

@bot.event
async def on_ready():
  print('로딩완료')
  await bot.change_presence(activity=discord.Game("?도움"))

#docs
@bot.command()
async def join(ctx):
  db[f"{ctx.author.id}"] = 0
  await ctx.reply('가입이 완료되었습니다.')

@bot.command()
async def 문제(ctx):
  value = db[f"{ctx.author.id}"]

  if value == None:
    await ctx.reply('`?join` 명령어를 먼저 실행해주세요!')
    return None


  a = random.randrange(1,5)
  if a == 1:
    a = random.randrange(1,50)
    b = random.randrange(1,50)
    await ctx.send(f'**덧셈문제**\n> {a} + {b} = ?')
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await ctx.reply('타임아웃!!')
      return None

    else:
      c = str(a + b)
      if msg.content == c:
        value = value + 100
        db[f"{ctx.author.id}"] = value
        await ctx.send(f'**정답!**\n> 100point가 적립되었습니다!(보유금액 : {value})')
        
      else:
        await ctx.send(f'**아쉽네요!**\n> 정답 : {c}')

  elif a == 2:
    a = random.randrange(1,50)
    b = random.randrange(1,50)
    await ctx.send(f'**뺄셈문제**\n> {a} - {b} = ?')
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await ctx.reply('타임아웃!!')
      return None

    else:
      c = str(a - b)
      if msg.content == c:
        value = value + 100
        db[f"{ctx.author.id}"] = value
        await ctx.send(f'**정답!**\n> 100point가 적립되었습니다!(보유금액 : {value})')
        
      else:
        await ctx.send(f'**아쉽네요!**\n> 정답 : {c}')

  elif a == 3:
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    await ctx.send(f'**곱셈문제**\n> {a} X {b} = ?')
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await ctx.reply('타임아웃!!')
      return None

    else:
      c = str(a * b)
      if msg.content == c:
        value = value + 100
        db[f"{ctx.author.id}"] = value
        await ctx.send(f'**정답!**\n> 100point가 적립되었습니다!(보유금액 : {value})')
        
      else:
        await ctx.send(f'**아쉽네요!**\n> 정답 : {c}')
  
  if a == 4:
    a = random.randrange(1,51, 2)
    b = random.randrange(1,51, 2)
    await ctx.send(f'**나눗셈문제**(단 소숫점은 버린다)\n> {a} / {b} = ?')
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await ctx.reply('타임아웃!!')
      return None

    else:
      c = int(str(a / b))
      if msg.content == c:
        value = value + 100
        db[f"{ctx.author.id}"] = value
        await ctx.send(f'**정답!**\n> 100point가 적립되었습니다!(보유금액 : {value})')
        
      else:
        await ctx.send(f'**아쉽네요!**\n> 정답 : {c}')

@bot.command()
async def 삭제(ctx):
  del db[f"{ctx.author.id}"]
  await ctx.send('회원정보가 삭제되었어요!')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send('`?join`을 먼저 해주세요!')

@bot.command()
async def 정보(ctx):
  value = db[f"{ctx.author.id}"]
  await ctx.reply(f'<@!{ctx.author.id}>님이 가지고 계신 포인트 : `{value}point`')

@bot.command()
async def 도움(ctx): 
  await ctx.reply(f'1. `?join` : 가입을 진행합니다.\n2. `?정보` : 자신이 보유한 포인트 수를 확인합니다.\n3. `?문제` : 사칙연산 중 한 문제를 냅니다.\n4. `?탈퇴` : 회원정보를 삭제합니다.\n \n**주의사항 : 가입이 완료된 상태에서 가입을 하면 모든 포인트가 다 사라집니다.**')


bot.run('Token')
