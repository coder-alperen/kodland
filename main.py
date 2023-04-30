
import discord
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)


# Bot hazır olduğunda adını yazdıracak!
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('*hello'):
        await message.channel.send('Selam! Ben bir botum!')
    elif message.content.startswith('*smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('*coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('*pass'):
        await message.channel.send(sifre_olusturucu(10))
    else:
        await message.channel.send("Bu komutu anlayamadım :(")

client.run("")