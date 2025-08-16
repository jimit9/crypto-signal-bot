import requests
import time

# === CONFIG ===
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Replace with your Telegram ID (@jimitt)

def send_signal():
    message = "🚀 Test Signal\nPair: BTC/USDT\nAction: BUY\nSL: 2%\nTarget: 5%"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=payload)
    print("Sent:", response.json())

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(3600)  # sends every 1 hour for demo
