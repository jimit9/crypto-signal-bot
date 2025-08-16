import os
import requests
import time

# Read env variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN:", BOT_TOKEN)
print("CHAT_ID:", CHAT_ID)

# Function to send Telegram messages
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    print("Telegram API response:", resp.text)
    return resp.json()

# Send startup test message
try:
    send_telegram_message("🚀 Bot Started Successfully on Railway ✅")
except Exception as e:
    print("Error sending startup message:", e)

# Dummy loop (replace with your trading logic later)
while True:
    print("Bot running...")  
    time.sleep(60)
