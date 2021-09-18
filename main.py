import os
import discord
import requests
import json
from keep_awake import keep_awake

def get_news():
  query={
    "sources": "Axios",
    "apiKey": os.environ['APIKEY']
  }
  response=requests.get("https://newsapi.org/v2/top-headlines", params=query)
  bbc_page=response.json()
  article=bbc_page["articles"]
  titles=[]
  urls=[]
  for ar in article:
    titles.append(ar["title"])
    urls.append(ar["url"])

  return(titles,urls)

client=discord.Client()
TOKEN=os.environ['DISC_TOKEN']
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith("$news"):
    results,urls=get_news()
    for i in range(5):
      await message.channel.send(f"{i+1}. {results[i]}\n")
      await message.channel.send(f"{urls[i]}\n")
      
keep_awake()
client.run(TOKEN)

