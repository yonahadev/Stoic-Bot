import discord,random
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

lines = open("quotes.txt",encoding="utf-8").readlines()[4:]
lines = [line for line in lines if line != "\n"]

quotes = []
authorImages = {"Marcus Aurelius":"https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTgxMDA5NzU3ODkxNDcwNDI0/marcus-aurelius-gettyimages-122316830.jpg",
"Epictetus":"https://dailystoic.com/wp-content/uploads/2018/04/epictetus.jpg",
"Seneca":"https://cdn.britannica.com/33/9433-050-C21D7F4F.jpg"}

num_quotes = len(lines)//3
for i in range(0,len(lines),3):
    quote = lines[i].replace("\n","")
    stoic = lines[i+1].replace("\n","")
    source = lines[i+2].replace("\n","")
    quotes.append((quote,stoic,source))

@bot.event
async def on_ready():
    print("Bot is up and running!")

@bot.command()
async def quote(ctx: commands.Context):
    quoteTuple = random.choice(quotes)
    quote,stoic,extract = quoteTuple
    e = discord.Embed(title=f"{stoic} - {extract}",description=quote,color=ctx.author.color)
    authorImage = authorImages[stoic]
    e.set_thumbnail(url=authorImage)
    await ctx.send(embed=e)

bot.run(token)