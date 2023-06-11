import discord
import os

TOKEN = 'you can enter your token here, but I suggest adding your token in an .env file where no one can see it'

client = discord.Client()

# Series lists for the server. Each variable is assigned different series depending on who is asking for what. (Replace the series with the ones you or your server want)
player1_list = ['Persona 5', 'Re:Zero kara Hajimeru Isekai Seikatsu', 'Kimetsu no Yaiba', 'Oyasumi Punpun' , 'Kanojo, Okarishimasu' , 'Hori-san to Miyamura-kun', 'Mushoku Tensei']
player2_list = ["Kimi to Boku no Saigo no Senjou", "Arui wa Sekai ga Hajimaru Seisen", "Fukakai na Boku no Subete wo", "Guilty Crown", "Tate no Yuusha no Nariagari" , "Ansatsu Kyoushitsu"]
player3_list = ["No Game No Life", "Overlord", "Shuumatsu Nani Shitemasu ka", "Kamisama ni Natta Hi", "Ascendance of a Bookworm", "Watashi ni Tenshi ga Maiorita!", "Tales of Demons and Gods", "Solo Leveling"]
player4_list = ['Fire Emblem', 'Kobayashi-san Chi no Maid Dragon', 'monster']
player5_list = ["Sin: Nanatsu no Taizai", "Kakegurui","Raise Kamika", "Yagate Kimi ni Naru", "Youjo Senki", "Hataage! Kemono Michi", "Machikado Mazoku", "Murenase! Shiiton Gakuen"]

# Event to know the program is running
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Event listener to check if the rolled character is on someones list. If it is, it pings the person
@client.event
async def on_message(message):
    # Checks who the message came from and from what channel. Adjust accordingly or remove
    if message.author == client.user:
        return
    if message.channel.id == ChannelID:
        return
    if message.channel.id == ChannelID:
        return
    if message.channel.id == ChannelID:
        return
    
    # Checks if the embed is greater than 0
    if len(message.embeds) > 0 and not message.embeds[0].Empty:

      # Looks for matches and pings the respective person
      for player1 in player1_list: 
        if player1 in message.embeds[0].description:
          await message.channel.send('A series from <@player1_discord_ID> list has been summoned but it doesnt matter since player3 is just gonna grab it :|')  
      for player2 in player2_list:
        if player2 in message.embeds[0].description:
          await message.channel.send('A series from <@player2_discord_ID> list has been summoned')
      for player3 in player3_list:
        if player3 in message.embeds[0].description:
          await message.channel.send('A series from <@player3_discord_ID> list has been summoned')
      for player4 in player4_list:
        if player4 in message.embeds[0].description:
          await message.channel.send('A series from <@player4_discord_ID> list has been summoned')
          
# Uses your token to run the program          
client.run(TOKEN)