from botlogic import gen_pass

print(gen_pass(10))

import discord
import random 

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$poluição'):
        await message.channel.send("A poluição é a introdução de substâncias ou energia no ambiente que causam danos aos seres vivos, à saúde humana e ao equilíbrio da natureza.")
    elif message.content.startswith('$tchau'):
        await message.channel.send("Tchau! tenha um bom dia")
    elif  message.content.startswith('$curiosidade do dia'):
        frases = [
            "A poluição é a introdução de substâncias nocivas no ambiente.",
            "Menos de 3 porcento da água da Terra é doce e própria para consumo.",
            "Plantar uma árvore ajuda a filtrar o ar e combater o aquecimento global.",
            "Evite o desperdício: use sacolas reutilizáveis!"
        ]
        escolha = random.choice(frases)
        await message.channel.send(escolha)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Pergunta'):
        questoes = [
            ["Qual destes materiais leva mais tempo para se decompor?", "A) Papel", "B) Plástico", "🇧"],
            ["O que é coleta seletiva?", "A) Separar o lixo por tipo", "B) Jogar tudo no mesmo saco", "🇦"],
            ["Economizar água ajuda o planeta?", "A) Sim, preserva recursos", "B) Não faz diferença", "🇦"]
        ]
        
        q = random.choice(questoes)
        texto_pergunta = f"**DESAFIO DO DIA**\n\n{q[0]}\n\n{q[1]}\n{q[2]}"
        
        msg = await message.channel.send(texto_pergunta)
        await msg.add_reaction("🇦")
        await msg.add_reaction("🇧")


CARGO_NIVEL_1 = 1500148516100509806  # Ex: "Protetor Iniciante"
CARGO_NIVEL_2 = 1500148690126504107  # Ex: "Herói Ambiental"



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando de Pergunta
    if message.content.startswith('$pergunta'):
        # Pergunta, Opção A, Opção B, Resposta Correta
        questoes = [
            ["Onde se joga pilhas usadas?", "A) Lixo Comum", "B) Ponto de Coleta", "B"],
            ["Qual gasta mais água?", "A) Banho de 15 min", "B) Lavar as mãos", "A"]
        ]
        
        q = random.choice(questoes)
        await message.channel.send(f"**VALENDO PONTOS:**\n{q[0]}\n{q[1]}\n{q[2]}\n\n(Responda com apenas 'A' ou 'B')")

        # Função para esperar a resposta do usuário
        def check(m):
            return m.author == message.author and m.content.upper() in ['A', 'B']

        try:
            msg_resposta = await client.wait_for('message', check=check, timeout=30.0)
            
            if msg_resposta.content.upper() == q[3]:
                user_id = message.author.id
                # Adiciona 1 ponto
                pontos_usuarios[user_id] = pontos_usuarios.get(user_id, 0) + 1
                total = pontos_usuarios[user_id]
                
                await message.channel.send(f"✅ Acertou! Você agora tem {total} pontos.")

                # SISTEMA DE CARGOS
                guild = message.guild
                member = message.author

                if total == 5: # Ganha o primeiro cargo com 5 pontos
                    cargo = guild.get_role(CARGO_NIVEL_1)
                    await member.add_roles(cargo)
                    await message.channel.send(f"🎊 Parabéns {member.mention}! Você subiu para o cargo **{cargo.name}**!")
                
                elif total == 10: # Ganha o segundo cargo com 10 pontos
                    cargo = guild.get_role(CARGO_NIVEL_2)
                    await member.add_roles(cargo)
                    await message.channel.send(f"🌟 INCRÍVEL! {member.mention} agora é um **{cargo.name}**!")

            else:
                await message.channel.send("❌ Errado! Tente na próxima.")
        
        except:
            await message.channel.send("⏰ O tempo acabou! Responda mais rápido na próxima.")

client.run


# ... suas configurações de intents ...

# "Memória" do bot: {id_do_usuario: quantidade_de_pontos}
pontos_usuarios = {}


client.run("")
