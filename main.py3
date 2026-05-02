from botlogic import gen_pass

print(gen_pass(10))

import discord

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
    if message.content.startswith('67'):
        await message.channel.send("https://i.pinimg.com/1200x/11/ec/a5/11eca5fe79f248d6ad984564a71ab9f8.jpg")
    if message.content.startswith('oi bom dia'):
        await message.channel.send("https://pbs.twimg.com/media/G28LKLwaEAAMJAt.jpg")
client.run("MTQ5MjUxOTMwOTQyMjEwNDY4Ng.GXpfMZ.roOUQoND6vk0inWm88NJq4iL9fszJzjcq4EQL0")
