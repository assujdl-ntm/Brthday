import os
import discord
from discord.ext import tasks
from datetime import datetime
import json

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1459518772330106931

with open("birthdays.json", "r", encoding="utf-8") as f:
    birthdays = json.load(f)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@tasks.loop(hours=24)
async def check_birthdays():
    today = datetime.now().strftime("%d-%m")
    channel = client.get_channel(CHANNEL_ID)
    for name, date in birthdays.items():
        if date == today:
            await channel.send(f"🎂 Aujourd’hui c’est l’anniversaire de **{name}** !")

@client.event
async def on_ready():
    print("Bot connecté !")
    check_birthdays.start()

client.run(TOKEN)
