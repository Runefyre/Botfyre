
import asyncio
import discord
import random
import glob
import time
import random
import sys

client = discord.Client()

files = glob.glob("*.mp3")

@client.event
async def on_ready():
    if not discord.opus.is_loaded():
        discord.opus.load_opus()

    client.voice = None

    print('Logged in as')
    print(' ->  Name: '+client.user.name)
    print(' ->    ID: '+client.user.id)

@client.event
async def on_message(message):
    
    if message.content == '/summ':
        if client.voice:
            await client.voice.disconnect()
            client.voice = None
        for chan in message.server.channels:
            if chan.type == discord.ChannelType.voice and message.author in chan.voice_members:
                client.voice = await client.join_voice_channel(chan)
                await client.delete_message(message)

        while client.voice:
            await asyncio.sleep(random.randrange(30,60))
            player = client.voice.create_ffmpeg_player(files[random.randrange(len(files))])
            player.volume = 0.5
            player.start()


    elif message.content == '/test':
        if not client.voice:
            for chan in message.server.channels:
                if chan.type == discord.ChannelType.voice and message.author in chan.voice_members:
                    client.voice = await client.join_voice_channel(chan)

        if client.voice:
            player = client.voice.create_ffmpeg_player(files[random.randrange(len(files))])
            player.volume = 0.5
            player.start()
            await client.delete_message(message)

    elif message.content == '/disc':
        if client.voice:
            await client.voice.disconnect()
            client.voice = None
            await client.delete_message(message)

    elif message.content == '/words':
        await client.send_message(message.channel,'kek')
        await client.delete_message(message)

    elif message.content == '/help':
        hlp = "```Help for Botfyre:\n/summ = Summon the bot to your current voice channel.\n/disc = Disconnect the bot from it's current voice channel.\n/help = Show this help.\n/p2g <god> <relic> = Print a Path to Glory thing. I don't know what this is, ask Sasha.```"
        await client.send_message(message.channel,hlp)
        await client.delete_message(message)
        await asyncio.sleep(15)
        await client.delete_message(hlp)
        

    elif '/p2g' in message.content and message.author != client.user:
        god = message.content.split(' ', 2)[1].strip()
        relic = message.content.split(' ', 2)[2].strip()

        if (message.content.split(' ', 2)[1].strip()).capitalize() != 'Khorne' or (message.content.split(' ', 2)[1].strip()).capitalize() != 'Slaanesh' or (message.content.split(' ', 2)[1].strip()).capitalize() != 'Tzeentch' or (message.content.split(' ', 2)[1].strip()).capitalize() != 'Nurgle':
            #first part of name:
            nameloc1 = random.randint(0,35)
            f = open('p2g names.txt', 'r')
            name1 = f.read().splitlines()
            f.close
            #Second part of name:
            f = open('p2g names 2.txt', 'r')
            name2 = f.read().splitlines()
            f.close
            #Title:
            p = open('p2g titles.txt', 'r')
            lineno = p.read().splitlines()
 
            if god.capitalize() == 'Khorne':
                Title = lineno[random.randint(37, 72)]
            elif god.capitalize() == 'Tzeentch':
                Title = lineno[random.randint(74, 109)]
            elif god.capitalize() == 'Nurgle':
                Title = lineno[random.randint(111, 146)]
            elif god.capitalize() == 'Slaanesh':
                Title = lineno[random.randint(148, 183)]
            else:
                Title = lineno[random.randint(0, 35)]
            p.close
            temp = ('Your leader is ', name1[random.randint(0, 35)],name2[random.randint(0, 35)],' ', Title, ', Chaos Lord of ', god.capitalize())
            await client.send_message(message.channel,"".join(temp))

            #retinue

            if relic.capitalize() == 'Y':
                unitquant = random.randint(4, 6) - 1
            elif relic.capitalize() == 'N':
                unitquant = random.randint(4, 6)

            temp = ('You have ', str(unitquant), ' units in your warband:')       
            await client.send_message(message.channel,"".join(temp))
            f = open('Units.txt', 'r')
            unit = f.read().splitlines()
            x = 0
            while x < unitquant:
                cat = random.randint(1, 3)
                if cat == 1:
                    x = x + 1
                    choice = unit[random.randint(0, 35)]
                    if god.capitalize() == 'Khorne':
                        if choice == '9 Thousand Sons' or choice == '7 Plague Marines' or choice == '6 Noise Marines':
                            await client.send_message(message.channel,'8 Khorne Berzerkers')
                        else:
                            await client.send_message(message.channel,choice)
                    elif god.capitalize() == 'Tzeentch':
                        if choice == '7 Plague Marines' or choice == '8 Khorne Berzerkers' or choice == '6 Noise Marines':
                            await client.send_message(message.channel,'9 Thousand Sons')
                        else:
                            await client.send_message(message.channel,choice)
                    elif god.capitalize() == 'Nurgle':
                        if choice == '9 Thousand Sons' or choice == '8 Khorne Berzerkers' or choice == '6 Noise Marines':
                            await client.send_message(message.channel,'7 Plague marines')
                        else:
                            await client.send_message(message.channel,choice)
                    elif god.capitalize() == 'Slaanesh':
                        if choice == '9 Thousand Sons' or choice == '7 Plague Marines' or choice == '8 Khorne Berzerkers':
                            await client.send_message(message.channel,'6 Noise Marines')
                        else:
                            await client.send_message(message.channel,choice)
                    else:
                        await client.send_message(message.channel,choice)
            
                elif cat == 2:
                    x = x + 1
                    temp = unit[random.randint(37, 42)]
                    await client.send_message(message.channel,temp)
                elif cat == 3:
                    x = x + 1
                    #first part of name:
                    nameloc1 = random.randint(0,35)
                    f = open('p2g names.txt', 'r')
                    name1 = f.read().splitlines()
     
                    f.close
                    #Second part of name:
                    f = open('p2g names 2.txt', 'r')
                    name2 = f.read().splitlines()
                    f.close
                    #Title:
                    p = open('p2g titles.txt', 'r')
                    lineno = p.read().splitlines()
     
                    if god.capitalize() == 'Khorne':
                        Title = lineno[random.randint(37, 72)]
                    elif god.capitalize() == 'Tzeentch':
                        Title = lineno[random.randint(74, 109)]
                    elif god.capitalize() == 'Nurgle':
                        Title = lineno[random.randint(111, 146)]
                    elif god.capitalize() == 'Slaanesh':
                        Title = lineno[random.randint(148, 183)]
                    else:
                        Title = lineno[random.randint(0, 35)]
                    p.close
            
                    hero = unit[random.randint(44, 49)]
                    if hero != 'An Aspiring Follower':
                        temp = (hero, ': ', name1[random.randint(0, 35)],name2[random.randint(0, 35)],' ', Title)
                        await client.send_message(message.channel,"".join(temp))
                    elif hero == 'An Aspiring Follower':
                        temp = (hero, '; ', unit[random.randint(44, 48)], ': ', name1[random.randint(0, 35)],name2[random.randint(0, 35)],' ', Title)
                        await client.send_message(message.channel,"".join(temp))
                        
            await client.delete_message(message)

#@client.event
#async def on_voice_state_update(before,after):
#    print("something changed")
#    print(after.voice)

client.run("MTk1MjM2OTU1MDc4OTE4MTQ0.CzBuEw.crm44AZBOyOYVO8EYegLEf2nGKg", bot=True)
