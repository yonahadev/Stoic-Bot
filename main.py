import discord,random
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix="s ", intents = discord.Intents.all())

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
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game("s info"))
    print("Bot is up and running!")

@bot.command()
async def quote(ctx: commands.Context):
    quoteTuple = random.choice(quotes)
    quote,stoic,extract = quoteTuple
    e = discord.Embed(title=f"{stoic} [{extract}]",description=quote,color=ctx.author.color)
    authorImage = authorImages[stoic]
    e.set_thumbnail(url=authorImage)
    await ctx.send(embed=e)

@bot.command()
async def info(ctx: commands.Context):
    e = discord.Embed(title="Stoic Bot by goat6",description="*Hi, I'm the Stoic Bot - use **s quote** to receive a quotation*",color=ctx.author.color)
    e.set_thumbnail(url="https://avatars.githubusercontent.com/u/83908974?s=400&u=db2569c5c27ad88c35f02128b3433d21c8b16796&v=4")
    e.add_field(name="Credits",value="**Developed by:** https://github.com/goat6 **\nWith help from:** https://github.com/Spacerulerwill")
    await ctx.send(embed=e)

if __name__ == "__main__":
    bot.run(token)
