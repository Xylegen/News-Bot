import os
import discord
import requests
import json

#def get_quote():
 #response=requests.get("https://zenquotes.io/api/random")
 # json_data=json.loads(response.text)
 #quote=json_data[0]['q']+ " -" + json_data[0]['a']
  #return(quote)

def get_news():
  query={
    "sources": "Axios",
    "apiKey": "920ba8c3f59e4e369c6f12e914800c6d"
  }
  response=requests.get("https://newsapi.org/v2/top-headlines", params=query)
  bbc_page=response.json()
  article=bbc_page["articles"]
  titles=[]
  urls=[]
  for ar in article:
    titles.append(ar["title"])
  for ra in article:
    urls.append(ar["url"])

  return(titles,urls)



client=discord.Client()
TOKEN=os.environ['DISC_TOKEN']
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith("$news"):
   # quote=get_quote()
    results,urls=get_news()
    for i in range(5):
      await message.channel.send(f"{i+1}. {results[i]}\n")
      await message.channel.send(f"{urls[i]}\n")
    #mention=message.author.mention
    
    #await message.channel.send(f"{mention}, You got this homes!")

client.run(TOKEN)