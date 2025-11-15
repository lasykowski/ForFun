import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Zalogowano jako {client.user}")

@client.event
async def on_message(message):
    # Ignoruj wiadomości wysłane przez boty
    if message.author.bot:
        return

    await message.channel.send(
        f'Użytkownik {message.author.name} napisał: "{message.content}"'
    )

client.run("MTQzOTEwODA3Mjk5MDcwMzcwOQ.Gsakxu.c18WM_bb07cIIoIUs1E1AzDhs-XPFILtzkJq0k")
