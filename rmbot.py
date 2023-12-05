import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from datetime import timedelta
import datetime
import pytz
utc=pytz.UTC
import typing
import openpyxl
import time
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
discord

#SLASH COMMANDS
#COMANDO "PING"
@tree.command(name = "ping", description = "Test del bot", guild=discord.Object(id=1119937562123980820))
async def first_command(interaction):
    await interaction.response.send_message("Pong!")



#COMANDO "KICK"
@tree.command(name = "kick", description = "Espelli lo stronzo", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(member="L'ID dello stronzo",reason="Motivazione")
async def kick(interaction, member: discord.Member, reason: str):
    if member.bot:
        await interaction.response.send_message(content="Non puoi espellere un bot", ephemeral=True)
    elif  member.get_role(1119938660662517812)!=None:
        embed=discord.Embed(title="**L'utente "+member.name+" è stato espulso**", description="Motivazione: "+reason, color=0x002aff)
        embed.set_thumbnail(url=member.display_avatar.url)
        channel=client.get_channel(1120037425801068634)
        await channel.send(embed=embed)
        channel = await member.create_dm()
        embed=discord.Embed(title="**Sei stato espulso**", description="Motivazione: "+reason, color=0x002aff)
        await channel.send(embed=embed)
        await member.kick()
        await interaction.response.send_message(content="L'utente "+member.mention+" è stato espulso", ephemeral=True)
    else:
        await interaction.response.send_message(content="L'utente non è presente nel Server", ephemeral=True)



#COMANDO "BAN"
@tree.command(name = "ban", description = "Banna lo stronzo", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(member="L'ID dello stronzo",reason="Motivazione")
async def ban(interaction, member: discord.Member, reason: str):
    if member.bot:
        await interaction.response.send_message(content="Non puoi bannare un bot", ephemeral=True)
    elif  member.get_role(1119938660662517812)!=None:
        embed=discord.Embed(title="**L'utente "+member.name+" è stato bannato**", description="Motivazione: "+reason, color=0x002aff)
        embed.set_thumbnail(url=member.display_avatar.url)
        channel=client.get_channel(1120037425801068634)
        await channel.send(embed=embed)
        channel = await member.create_dm()
        embed=discord.Embed(title="**Sei stato bannato**", description="Motivazione: "+reason, color=0x002aff)
        await channel.send(embed=embed)
        await member.ban()
        await interaction.response.send_message(content="L'utente "+member.mention+" è stato bannato", ephemeral=True)
    else:
        await interaction.response.send_message(content="L'utente non è presente nel Server", ephemeral=True)



#COMANDO "UNBAN"
@tree.command(name = "unban", description = "Sbanna l'ex stronzo", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(member="L'ID dell'exstronzo",reason="Motivazione")
async def unban(interaction, member: discord.Member, reason: str):
    if member.bot:
        await interaction.response.send_message(content="Non puoi sbannare un bot", ephemeral=True)
    elif  member.get_role(1119938660662517812)!=None:
        embed=discord.Embed(title="**L'utente "+member.name+" è stato bannato**", description="Motivazione: "+reason, color=0x002aff)
        embed.set_thumbnail(url=member.display_avatar.url)
        channel=client.get_channel(1120037425801068634)
        await channel.send(embed=embed)
        channel = await member.create_dm()
        embed=discord.Embed(title="**Sei stato bannato**", description="Motivazione: "+reason, color=0x002aff)
        await channel.send(embed=embed)
        await member.unban()
        await interaction.response.send_message(content="L'utente "+member.mention+" è stato bannato", ephemeral=True)
    else:
        await interaction.response.send_message(content="L'utente non è presente nel Server", ephemeral=True)



#COMANDO "MUTE"
@tree.command(name = "mute", description = "Muta lo stronzo", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(member="Lo stronzo da mutare", reason="Motivo", secondi="Secondi del mute", minuti="Minuti del mute", ore="Ore del mute", giorni="Giorni del mute")
async def mute(interaction, member: discord.Member, reason: str, secondi: typing.Optional[int]=0, minuti: typing.Optional[int]=0, ore: typing.Optional[int]=0, giorni: typing.Optional[int]=0):
    if (secondi==0 and minuti==0 and ore==0 and giorni==0):
        await interaction.response.send_message(content="Hai messo 0 tempo, coglione", ephemeral=True)
    elif member.bot:
        await interaction.response.send_message(content="Non puoi mutare un bot", ephemeral=True)
    elif  member.get_role(1119938660662517812)!=None:
        embed=discord.Embed(title="**L'utente "+member.name+" è stato mutato**", description="Durata: "+str(giorni)+"d "+str(ore)+"h "+str(minuti)+"m "+str(secondi)+"s\nMotivazione: "+reason, color=0x002aff)
        embed.set_thumbnail(url=member.display_avatar.url)
        channel=client.get_channel(1120037425801068634)
        await channel.send(embed=embed)
        channel = await member.create_dm()
        embed=discord.Embed(title="**Sei stato mutato**", description="Durata: "+str(giorni)+"d "+str(ore)+"h "+str(minuti)+"m "+str(secondi)+"s\nMotivazione: "+reason, color=0x002aff)
        await channel.send(embed=embed)
        tempo=timedelta(seconds=secondi, minutes=minuti, hours= ore, days=giorni)
        await member.timeout(tempo)
        await interaction.response.send_message(content="L'utente "+member.mention+" è stato mutato per: "+str(giorni)+"d "+str(ore)+"h "+str(minuti)+"m "+str(secondi)+"s", ephemeral=True)
    else:
        await interaction.response.send_message(content="L'utente non è presente nel Server", ephemeral=True)



#COMANDO "UNMUTE"
@tree.command(name = "unmute", description = "Smuta lo stronzo", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(member="L'exstronzo da smutare")
async def unmute(interaction, member:discord.Member):
    timedout=member.timed_out_until.replace(tzinfo=utc)
    today=datetime.datetime.today().replace(tzinfo=utc)
    print(timedout)
    print(today)
    print(timedout<today)
    print(timedout>today)
    print(member.is_timed_out)
    if member.bot:
        await interaction.response.send_message(content="Non puoi mutare un bot", ephemeral=True)
    elif timedout<today:
        await interaction.response.send_message(content="L'utente non è mutato", ephemeral=True)
    elif  member.get_role(1119938660662517812)!=None:
        await member.timeout(None)
        await interaction.response.send_message(content="L'utente "+member.mention+" è stato smutato", ephemeral=True)
    else:
        await interaction.response.send_message(content="L'utente non è presente nel Server", ephemeral=True)



#COMANDO "ADDOROLEALL"
@tree.command(name="addroleall", description="Aggiungi un ruolo a tutti gli utenti", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(role="Il ruolo da aggiungere a tutti gli utenti")
async def addroleall(interaction, role:discord.Role):
    i=0
    guild=interaction.guild
    await interaction.response.send_message(content="Elaborazione: "+str(i)+" su "+str(len(guild.members)), ephemeral=True)
    for member in guild.members:
        if not(member.bot): await member.add_roles(member.guild.get_role(role.id))
        i+=1
        await interaction.edit_original_response(content="Elaborazione: "+str(i)+" su "+str(len(guild.members)))
    await interaction.edit_original_response(content="Programma terminato")


#COMANDO "ADDROLE"
@tree.command(name="addrole", description="Aggiungi un ruolo ad un utente", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(role="Il ruolo da aggiungere all'utente", member="L'utente")
async def addrole(interaction, role:discord.Role, member:discord.Member):
    await member.add_roles(member.guild.get_role(role.id))
    await interaction.response.send_message(content="Ruolo "+role.mention+" aggiunto a "+member.mention, ephemeral=True)



#COMANDO "CLEAR"
@tree.command(name="clear", description="Cancella un massimo di 100 messaggi", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(num="Numero di messaggi (max 100)")
async def clear(interaction, num:int):
    channel=client.get_channel(interaction.channel_id)
    if (num<1 or num>100): await interaction.response.send_message(content="Numero di messaggi errato, riprovare", ephemeral=True)
    else:
        await interaction.response.send_message(content=str(num)+" messaggi cancellati", ephemeral=True)
        await channel.purge(limit=num)



#COMANDO "ANNUNCIO"
@tree.command(name="annuncio", description="Comando per creare un annuncio embed", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(channel="Canale dove inviare l'annuncio", title="Titolo dell'annuncio", description="Descrizione dell'annuncio", image="URL immagine", thumbnail="URL thumbnail", link="URL per il link nel titolo dell'embed")
async def annuncio(interaction, channel:discord.TextChannel, title:str, description:str, image:typing.Optional[str]="", thumbnail:typing.Optional[str]="", link:typing.Optional[str]=""):
    embed=discord.Embed(title="**"+title+"**", description=description, url=link, color=0x002aff)
    if image!="":embed.set_image(url=image)
    if thumbnail!="":embed.set_thumbnail(url=thumbnail)
    channel=client.get_channel(channel.id)
    await channel.send(embed=embed)
    await interaction.response.send_message(content="Annuncio inviato", ephemeral=True)



#COMANDO "SONDAGGIO"
@tree.command(name="sondaggio", description="Comando che crea un sondaggio", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(channel="Canale dove inviare il sondaggio", title="Titolo del sondaggio")
async def sondaggio(interaction, channel:discord.TextChannel, title:str, emojia:typing.Optional[str]="", optiona:typing.Optional[str]="", emojib:typing.Optional[str]="", optionb:typing.Optional[str]=""):
    description=""
    if (emojia!="" and optiona!=""): description+=emojia+" "+optiona+"\n"
    if (emojib!="" and optionb!=""): description+=emojib+" "+optionb+"\n"
    embed=discord.Embed(title="**"+title+"**", description=description)
    channel=client.get_channel(channel.id)
    message=await channel.send(embed=embed)
    await message.add_reaction(str(emojia))
    await message.add_reaction(str(emojib))



#RUOLI PULSANTE
messageidforcolorrole=0
messageidforstaff=0
#INVIO MESSAGGIO RECATION ROLE
@tree.command(name="sendreactioncolorrole", description="Invia un messaggio con i reaction role dei colori", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(channel="Canale dove inviare i reaction roles")
async def sendreactionrole(interaction, channel:discord.TextChannel):
    embed=discord.Embed(title="**Scegli il colore del tuo profilo!!!**", description="Clicca sulla reazione corrispondente al colore del ruolo che vuoi, se vuoi qualche altro colore chiedi ad un membro dello staff; infine se vuoi togliere il colore dal tuo profilo, basta ricliccare sul colore già presente")
    message=await channel.send(embed=embed)
    await interaction.response.send_message(content="Reaction Color Role inviato", ephemeral=True)
    await message.add_reaction(str("🟪"))
    await message.add_reaction(str("🟥"))
    await message.add_reaction(str("🟧"))
    await message.add_reaction(str("🟦"))
    await message.add_reaction(str("⬛"))
    global messageidforcolorrole
    messageidforcolorrole=message.id


#SET ID REACTION ROLE
@tree.command(name="setidreactionrole", description="(NON USARE QUESTO COMANDO SE NON SAI COSA FA)", guild=discord.Object(id=1119937562123980820))
async def sendreactionrole(interaction, num:int):
    global messageidforcolorrole
    messageidforcolorrole=num
    await interaction.response.send_message(content="ID messaggio reactioncolorrole impostato", ephemeral=True)


#AGGIORNA I MEMBRI




#ROLE CONTROLLER
@client.event
async def on_raw_reaction_add(payload):
    emojirole={
        discord.PartialEmoji(name='🟧'):1146436873582018621,
        discord.PartialEmoji(name='🟪'):1146747899263320134,
        discord.PartialEmoji(name='🟥'):1146747985410134076,
        discord.PartialEmoji(name='🟦'):1147176358104006666,
        discord.PartialEmoji(name='⬛'):1147176472998596678,
    }
    global messageidforcolorrole
    if payload.message_id==messageidforcolorrole:
        member=payload.member
        channel=client.get_channel(payload.channel_id)
        message=await channel.fetch_message(payload.message_id)
        if not(payload.emoji in emojirole): await message.clear_reaction(payload.emoji)
        else:
            if not((member.guild.get_role(emojirole[payload.emoji])) in member.roles):
                for i in emojirole:
                    if str(i) in str(member.roles): await member.remove_roles(member.guild.get_role(emojirole[i]))
                await member.add_roles(member.guild.get_role(emojirole[payload.emoji]))
            else: await member.remove_roles(member.guild.get_role(emojirole[payload.emoji]))
            await message.remove_reaction(payload.emoji, member)
    elif payload.message_id==messageidforstaff:
        channel=client.get_channel(payload.channel_id)
        guild=client.get_guild(1119937562123980820)
        category = client.get_channel(1179169810249158717)
        message=await channel.fetch_message(payload.message_id)
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        guild.get_member(payload.member.id): discord.PermissionOverwrite(read_messages=True)
        }
        channel= await category.create_text_channel(name="Canale staff"+payload.member.name,overwrites=overwrites)
        embed=discord.Embed(title="**Info Curriculum**", color=0x002aff,description="Ecco una rapida guida sulle info da dare:\nNome utente:\nEtà:\nEsperienze precedenti:\nCosa sai fare e cosa non sai fare riguardo al ruolo di admin:\n")
        await channel.send(embed=embed)
        await message.remove_reaction(payload.emoji, payload.member)


#SLASH COMMAND PER EVENTO STAFF
@tree.command(name="sendstaff", guild=discord.Object(id=1119937562123980820))
@app_commands.describe(channel="Canale di invio messaggio")
async def testfunction(interaction, channel:discord.TextChannel):
    embed=discord.Embed(title="**Ruoli Staff aperti!!!**", color=0x002aff, description="Da ora è disponibile il ruolo Admin, la quale avrà il compito di controllare il server, accertarsi il rispetto delle regole e aiuto su manuntenzione e gestione generale del server.\nSe siete interessati cliccate il tasto qui sotto per inviare una vostra domanda di assunzione!!!")
    message=await channel.send(embed=embed)
    await interaction.response.send_message(content="Messaggio creato", ephemeral=True)
    await message.add_reaction(str("📨"))
    global messageidforstaff
    messageidforstaff=message.id





#EVENTO MEMBRO ENTRATO NEL SERVER
@client.event
async def on_member_join(member):
    embed=discord.Embed(title="**Benvenuto**", description=member.mention+"!!!", color=0x002aff)
    embed.set_thumbnail(url=member.display_avatar.url)
    guild=client.get_guild(1119937562123980820)
    memberchannel=client.get_channel(1147658085201092688)
    await memberchannel.edit(name="Membri: "+str(guild.member_count))
    channel=client.get_channel(1120014820473839636)
    await channel.send(embed=embed)
    await member.add_roles(member.guild.get_role(1119938660662517812))
    print(member.name+" è entrato nel server")
#EVENTO MEMBRO USCITO DAL SERVER
@client.event
async def on_member_remove(member):
    embed=discord.Embed(title="**Addio**", description=member.mention, color=0x002aff)
    guild=client.get_guild(1119937562123980820)
    embed.set_thumbnail(url=member.display_avatar.url)
    memberchannel=client.get_channel(1147658085201092688)
    await memberchannel.edit(name="Membri: "+str(guild.member_count))
    channel=client.get_channel(1137508111117193227)
    await channel.send(embed=embed)
    print(member.name+" è uscito dal server")

#CONFERMA CONNESSIONE BOT
@client.event
async def on_ready():
    attivita=discord.Activity(type=discord.ActivityType.playing, name="Sta rubando i tuoi dati")
    print(f'{client.user} si è connesso a Discord!')
    await tree.sync(guild=discord.Object(id=1119937562123980820))
    await client.change_presence(status=discord.Status.online, activity=attivita)
        

client.run(TOKEN)