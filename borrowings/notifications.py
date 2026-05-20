import os
import requests


def send_telegram_message(message_text):
    # 1. Pull tokens from environment variables for security
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # 2. Guard clause: if credentials aren't set, log a warning instead of crashing
    if not bot_token or not chat_id:
        print("Telegram settings missing. Notification skipped.")
        return None

    # 3. Build the Telegram API endpoint URL
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # 4. Formulate the data payload
    payload = {
        "chat_id": chat_id,
        "text": message_text,
    }

    try:
        # 5. Fire the network request with a short timeout so your app never hangs
        response = requests.post(url, json=payload, timeout=5)
        return response
    except requests.RequestException as e:
        print(f"Failed to send Telegram notification: {e}")
        return None