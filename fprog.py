import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Your Token Here') # Replace with your own token.
import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
async def on_message(self, message):
  if message.author == self.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello World!')
{
  "postLink": "https://redd.it/w0teq0",
  "subreddit": "me_irl",
  "title": "me_irl",
  "url": "https://i.redd.it/ztpkxx6yl0c91.png",
  "nsfw": false,
  "spoiler": false,
  "author": "ozgonngu",
  "ups": 110,
  "preview": [
    "https://preview.redd.it/ztpkxx6yl0c91.png?width=108\u0026crop=smart\u0026auto=webp\u0026s=e3db2a1ed5ee73480224b55b16fcb38925ea9095",
    "https://preview.redd.it/ztpkxx6yl0c91.png?width=216\u0026crop=smart\u0026auto=webp\u0026s=aaec73a28c4c0b2bc47f4f9722be2fdb8ba95893",
    "https://preview.redd.it/ztpkxx6yl0c91.png?width=320\u0026crop=smart\u0026auto=webp\u0026s=90495a39d05f6d9d8975fb776887c08f65ece2c4",
    "https://preview.redd.it/ztpkxx6yl0c91.png?width=640\u0026crop=smart\u0026auto=webp\u0026s=b291abfb8f85b5826f001dee881570e694bdb46c",
    "https://preview.redd.it/ztpkxx6yl0c91.png?width=960\u0026crop=smart\u0026auto=webp\u0026s=7afc3f2532c7017a0045ae50777a18a2e452183e",
  ],
}
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']
import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Your Token Here') 