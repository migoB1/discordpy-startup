from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

goroku_a=[
"やぁ",
"あいぱっよ",
"ぴよぴよー",
"把握了",
"誤爆了",
"✌️三✌️",
"▂▅▇█▓▒░(‘ω’)░▒▓█▇▅▂　うわあああああああああ",
"[アラーム発生：ino（ととたま）]:./sound/alarm.mp3",
"(#＾ω＾)ﾋﾟｷﾋﾟｷ",
"やったぜ(´◜ω◝` )",
"(  ＾ω＾)・・・",
"(*’ω’ﾉﾉﾞ☆ﾁｬﾁｬﾁｬ",
"☜(`o´)コラコラ～",
"三('ω')三(ε: )三(.ω.)三(:3 )三('ω')三(ε: )三(.ω.)三(:3 )三ｺﾞﾛｺﾞﾛ",
"('ω')ﾌｧｯ",
"(੭ु´͈ᐜ`͈)੭ु⁾⁾",
"(๑°⌓°๑)",
"こっここりーこっこりーんっんっるるーてててて　てーててーてててこりー",
"˚₊*̥(∗*⁰͈꒨⁰͈)‧˚₊*̥",
"あえいでんてぃてぃ",
"(._. )(･_･)(･_･)(･_･)ｱﾚ?",
"(〃⌒∇⌒)ゞえへへっ♪",
"(´^ω^｀)ﾆﾁｬｱ",
"めうがみんなの心の火を燃やしているめう",
"ムリだなw",
"グルにきはとんでもないホモ||サピエンス||",
"く、来るさんがグル...!",
"グモニキはホル",
"うわああ!飛ばされちゃう〜",
"(｣・ω・)｣う…(｣・ω・)｣…─(─・ω・)─ｽｯ┌(┌・ω・)┐ﾀﾞﾝｯ┌(┌^o^)┐ﾎﾓｫ…﻿",
"ふーんえっちじゃん",
"ボスのおじ姦ー",
"わいはわいをすこt...",
"GURU×1",
"キレそうめう",
"だろw",
"気にしてないワン",
"アツゥイ！"]

@bot.command()
async def ping(ctx):
    aaa=random.randrange(len(goroku_a))
    await ctx.send(goroku_a[aaa])


bot.run(token)
