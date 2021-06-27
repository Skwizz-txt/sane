import discord
from discord.ext import commands
import random
import time

token = "you wont get it"
prefix = "s!"

sane = commands.Bot(command_prefix=prefix,description="Sane by Skwizz")
@sane.event
async def on_ready():
    print("Sane Hop In :) ")


@sane.command()
async def hi(ctx):
    await ctx.send(" Hiii :> ")


@sane.command()
async def infos(ctx):
    server = ctx.guild
    texts = len(server.text_channels)
    voice = len(server.voice_channels)
    members = server.member_count
    name = server.name
    embed = discord.Embed(title='**infos**',description="Infos about the server")
    embed.add_field(name="Your server : ",value=name)
    embed.add_field(name="Texts Channels : ",value=texts)
    embed.add_field(name="Voice Channels : ",value=voice)
    embed.add_field(name="Members : ",value=members)
    
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp)
    embed.set_footer(text="Lorem Ipsum")
    await ctx.send(embed = embed)


@sane.command()
async def say(ctx,*text):
    await ctx.send(" ".join(text))


@sane.command()
async def clear(ctx,number : int):
    messages = await ctx.channel.history(limit = number+1).flatten()
    for message in messages:
        await message.delete()
    embed = discord.Embed(title="**Clear**",description="Infos about clear command")
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp)
    embed.add_field(name="Message clears : ",value=number)
    embed.set_footer(text="Lorem Ipsum")
    sent = await ctx.send(embed = embed)
    
@sane.command()
async def lc(ctx,user):
    love = random.randint(0,100)
    embed = discord.Embed(title="**Love Calculator :heart: **",description="A new couple comming ? :heart: ")
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp)
    embed.add_field(name="love % : ",value=love,inline=False)
    if love >=50:
        embed.set_footer(text="A new relationship is possible :>")
    else:
        embed.set_footer(text="This is kinda low but don't give up :> ")
    await ctx.send(embed = embed)


@sane.command()
async def ban(ctx, user : discord.User,*reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title = "**User Banned**",description = "The over power of da ban")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/798282436844584960/888c8fc8b751e902935bc030821c9779.png?size=128")
    embed.set_author(name="Sane",url="https://cdn.discordapp.com/avatars/798282436844584960/888c8fc8b751e902935bc030821c9779.png?size=128")
    embed.add_field(name="Banned Member : ",value=user.name, inline=False)
    embed.add_field(name="Reason : ",value = reason)
    embed.add_field(name = "Moderator Who Banned : ",value = ctx.author.name)
    embed.set_footer(text="Lorem Ipsum")
    await ctx.send(embed = embed)

@sane.command()
async def kiss(ctx,user):
    choices = ["https://thumbs.gfycat.com/PersonalUnlinedAsiaticwildass-size_restricted.gif","https://i.pinimg.com/originals/e3/b5/63/e3b56398920f7a8f3314d9ae9baa0956.gif",
    "https://i0.wp.com/gifimage.net/wp-content/uploads/2017/09/anime-forehead-kiss-gif-10.gif?resize=650,400","https://i.pinimg.com/originals/a2/f8/f9/a2f8f98eb227321d2c76ae4be3e85fcf.gif",
    "https://i1.wp.com/nileease.com/wp-content/uploads/2021/03/0939ae60d616a4c7265da52e4abd0089.gif?fit=498%2C284&ssl=1","https://thumbs.gfycat.com/HopefulFabulousKouprey-max-1mb.gif",
    "https://i.pinimg.com/originals/e1/4e/4d/e14e4db9945815e67bffff69bf0b8df6.gif","https://i.pinimg.com/originals/e3/4e/31/e34e31123f8f35d5c771a2d6a70bef52.gif","https://i.imgur.com/4AaMn5E.gif",
    "https://i.pinimg.com/originals/4a/40/0f/4a400fc58c144fce01f6f2c54319222d.gif","https://media.tenor.com/images/e11e607335c7e9e265d4dbbdbb2bfdf5/tenor.gif"
    
    
    ]
    choosed = random.choices(choices)
    message = ctx.message.author.name,"you kissed",user,"<3"
    await ctx.send(" ".join(message))
    await ctx.send(" ".join(choosed))
@sane.command()
async def slap(ctx,user):
    choices = ["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b02c16d5-1b1b-4139-92e6-ca6b3d768d7a/d6wv007-5fbf8755-5fca-4e12-b04a-ab43156ac7d4.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2IwMmMxNmQ1LTFiMWItNDEzOS05MmU2LWNhNmIzZDc2OGQ3YVwvZDZ3djAwNy01ZmJmODc1NS01ZmNhLTRlMTItYjA0YS1hYjQzMTU2YWM3ZDQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.4MVfHXfzK83yI6L2NpBfVb2knaJtyGd7TlSEDH79bH8",
    "https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif?itemid=17314633","https://i.pinimg.com/originals/fe/39/cf/fe39cfc3be04e3cbd7ffdcabb2e1837b.gif","https://i.gifer.com/WpWp.gif",
    "https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif","https://i.gifer.com/B2Sm.gif","http://33.media.tumblr.com/4a58a89eaaea25571fcc03d3788b1e55/tumblr_nel3qwSzqw1tblzm8o1_500.gif",
    "https://i.imgur.com/fm49srQ.gif","https://thumbs.gfycat.com/DefiantBlindHyena-max-1mb.gif","https://thumbs.gfycat.com/AfraidDependentBrocketdeer-size_restricted.gif","https://media1.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif"]
    message = ctx.message.author.name,"you slaped",user,"BAM"
    await ctx.send(" ".join(message))
    choosed = random.choices(choices)
    await ctx.send("".join(choosed))

@sane.command()
async def command(ctx):
    message = "Here are the commands",ctx.message.author.mention
    await ctx.send(" ".join(message))
    embed = discord.Embed(title="**Commands Help**",description="Page 1")
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp)
    embed.add_field(name="**Hi**",value="This command simply say hi ^^",inline=False)
    embed.add_field(name="**Infos**",value="Show the servers infos as an embed",inline=False)
    embed.add_field(name="**Say**",value="Makes the bot say your following message",inline=False)
    embed.add_field(name="**Clear (number)**",value="Clear ( number ) past messages",inline=False)
    embed.set_footer(text="This is the page 1, type s!command2 for page 2")
    await ctx.send(embed=embed)
@sane.command()
async def command2(ctx):
    message = "Here are the commands ( page 2 ) ",ctx.message.author.mention
    await ctx.send(" ".join(message))
    embed = discord.Embed(title="**Commands Help**",description="Page 2")
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp)
    embed.add_field(name="**Ban (@user) (reason) **",value="Simply ban the user with the reason (reason) reason facultative",inline=False)
    embed.add_field(name="**Kiss (@user)**",value="Give a kiss to the user",inline=False)
    embed.add_field(name="**Slap (@user)**",value="SLAP THE USER !! ",inline=False)
    embed.add_field(name="**Command (number)**",value="Show the commands infos ( page = number )",inline=False)
    embed.set_footer(text="This is the page 2, type s!command3 for page 3",)
    await ctx.send(embed = embed)

@sane.command()
async def command3(ctx):
    message = "Here are the commands (page 3)",ctx.message.author.mention
    await ctx.send(" ".join(message))
    embed = discord.Embed(title="**Commands Help**",description="Page 3")
    embed.set_thumbnail(url=bot_pfp)
    embed.set_author(name="Sane",url=bot_pfp
    embed.add_field(name="**Lottery**",value="Play the lottery and maybe win ?? :p",inline=False)
    embed.set_footer(text="This is the page 3 type s!command for page 1.")
    await ctx.send(embed = embed)
@sane.command()
async def lottery(ctx):
    choices = ["You won a kiss !\n https://media.tenor.com/images/7bf94ea0f02bd107b531edc9e4006d85/tenor.gif ","You won a pat !\nhttps://thumbs.gfycat.com/BlankGiftedBurro-size_restricted.gif"
        "GG ! you won an uncomon : nothing..."
        ]
    
        
    lott = ["🍀","❌"]
    choice1 = random.choice(lott)
    choice2 = random.choice(lott)
    choice3 = random.choice(lott)
    message = choice1,choice2,choice3
    await ctx.send(" ".join(message))   
    if choice1 == "🍀" and choice2 == "🍀" and choice3 == "🍀":
        message = "GG ! ",ctx.message.author.mention,"You won !"
        await ctx.send(" ".join(message))
        choicewin = random.choice(choices)
        await ctx.send(choicewin)
    else:
        await ctx.send("No luck, you loosed...")





bot_pfp = "https://cdn.discordapp.com/avatars/798282436844584960/888c8fc8b751e902935bc030821c9779.png?size=128"
sane.run(token)
