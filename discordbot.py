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
"恥をすてろ",
"にゃるほどほてぷー",
"ふざけんな！(声だけ迫真)",
"グホ！",
"いやんほほ、ええやろ",
"てこっ",
"・:*三(　ε:)`дﾟ)･;",
"ぴよぴよー",
"把握了",
"誤爆了",
"喘がないで",
"✌️三✌️",
"▂▅▇█▓▒░(‘ω’)░▒▓█▇▅▂　うわあああああああああ",
"[アラーム発生：ino（ととたま）]:./sound/alarm.mp3",
"(#＾ω＾)ﾋﾟｷﾋﾟｷ",
"やったぜ(´◜ω◝` )",
"(  ＾ω＾)・・・",
"やったね⸜(๑⃙⃘'ᵕ'๑⃙⃘)⸝⋆*",
"(･ω･三･ω･)ﾌﾝﾌﾝ\n((⊂(∩///˙꒳​˙///∩)⊃))ﾌﾝﾌﾝ",
"射殺了",
"何回もシベリア行けて嬉しいな！！",
"ぽぽぽぽーん",
"わしゃわしゃするだけよ\n(  >ω<)ヾ(･ω･^ヾ)ﾜｼｬﾜｼｬ♡",
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
"しわピカ超ヤバくない？\nわかる〜まじ卍って感じ〜？",
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
"そうだよ(便乗)",
"ああ^〜いいっすね〜",
"当たり前だよなぁ",
"あくしろよ",
"あ(察し)",
"俺もやったんだからさ(嫌々)",
"かわいいかよぉ",
"多少はね?",
"誰がオタクや",
"もっと草生やしてけ？？？？",
"ちかっとちかっとちかちか！\nアッー",
"うぃんなーどうや？濃厚なミルクもあるで？ (*´Д`)ﾊｧﾊｧ",
"説明しよう！個性とは!・・・・・・・・・・・・・・・・・・・\nzzz\n以上である！",
"こんばんみっ✩°｡⋆⸜(* ॑꒳॑*  )⸝★",
"ムリだなw",
"絶対ホモにはならないからな",
"てっててってれー\nととたまのかしこさが1上がった!",
"のろぴ可愛いよー",
"ぺろぺろ",
"地縛了",
"あかうんこ",
"BBQ了",
"🍞🍞🐼ズンズンズンズン🐼\n🍞🍞🐼🍞🐼",
"Command pingってのがあまりしっくり来ないから他に何か良いコマンドありませんかね？ is not found",
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
"えへへえ",
"みとけみとけよー",
"自爆了",
"あっ(昇天)",
"うぎゃぁぁぁぁ\n暇ァァァァ\nうわぁぁぁぁぁ",
"あったまきた……(冷静)",
"ひゅみゅう",
"マインと結婚したい",
"他人が泣いていると私は元気になるのでもっと苦しんで欲しいくず〜(清々しい屑)",
"忘れろ忘れろ忘れろビーーーム",
"うわっ\nうん、頑張ってね…",
"スコレスのレスこれすこれすこれすこれすこれすこれ",
"ひゃー///",
"(๑•﹏•๑｀)ぷえ〜っ",
"グルさんを見てみなよ！",
"止まるんじゃねぇぞ…",
"GooGURU×2マップ",
"(ﾟ∀ﾟ)o彡゜しゃーさん！しゃーさん！",
"やっぱりホモじゃないか(歓喜)",
"ごめん、同級会にはいけません。今、シンガポールにいます。この国を南北に縦断する地下鉄を作っています。......本当は、あの頃が恋しいけれど、でも今はもう少しだけ、知らないふりをします。私の作る地下鉄も、きっといつか誰かの青春を乗せるから ",
"売り棒",
"まず景気づけに爆発します、そのあと程よいところで爆発します、最後になんとなく爆発します",
"待ちたまえ\n乗っていけよ",
"今日は爆発したい気分なの♡",
"溶けてらー",
"アツゥイ！"]


@bot.command()
async def ping(ctx):
    aaa=random.randrange(len(goroku_a))
    await ctx.send(goroku_a[aaa])


bot.run(token)
