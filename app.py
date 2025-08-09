import os, threading
from flask import Flask

# ----- Flask -----
app = Flask(__name__)

@app.get("/")
def home():
    return "Flask + Bot are running ✅"

def run_flask():
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)

# ----- Discord Bot (example using discord.py) -----
import discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

def run_bot():
    client.run(os.environ[""])

# ----- Start both -----
if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    run_flask()
