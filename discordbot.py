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
"あいぱっよ!",
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
"コ↑コ↓",
"(｣・ω・)｣う…(｣・ω・)｣…─(─・ω・)─ｽｯ┌(┌・ω・)┐ﾀﾞﾝｯ┌(┌^o^)┐ﾎﾓｫ…﻿",
"ふーんえっちじゃん",
"ボスのおじ姦ー",
"星五にしようね",
"GURU×1",
"キレそうめう",
"だろw",
"気にしてないワン",
"あそべー",
"やめて！やめて！あ▼は〜ん",
"ｱｱﾝｵｵﾝ！？！？！？",
"のろしもそう思います",
"💪(ᐛ💪)ﾔﾝﾉｶｵﾗｧ",
"(ᐛ)🖕",
"(ᐛ👐)ﾊﾟｧ",
"```ぺー神を崇めよ```",
"🖕(ᐛ  )🥤ｼﾞｬﾝｹﾝﾎﾟﾝ",
"もっと草生やしてけ？？？？",
"ちかっとちかっとちかちか！\nアッー",
"うぃんなーどや？濃厚なミルクもあるで？ (*´Д`)ﾊｧﾊｧ",
"説明しよう！個性とは!・・・・・・・・・・・・・・・・・・・\nzzz\n以上である！",
"こんばんみっ✩°｡⋆⸜(* ॑꒳॑*  )⸝★",
"ムリだなw",
"絶対ホモにはならないからな",
"てっててってれー\nととたまのかしこさが1上がった!",
"のろぴ可愛いよー",
"ぺろぺろ",
"呪殺了",
"ナニコレ\n君だよ",
"えびざんまい",
"いくいく\n810",
"ゆるさねぇ",
"素材化不可避ってね",
"アリアくんを崇め、敬い、そして脱がしなさい",
"やってみろよ!",
"煽ってけw",
"あー!水素の音ぉ〜!",
"(✋˘ω˘ 👌)大丈夫だ問題ない",
"アツゥイ！"]

@bot.command()
async def ping(ctx):
    aaa=random.randrange(len(goroku_a))
    await ctx.send(goroku_a[aaa])


bot.run(token)
