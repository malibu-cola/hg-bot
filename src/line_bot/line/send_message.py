import os
import requests

def send_line(text: str) -> None:
    token = os.getenv("CHANNEL_ACCESS_TOKEN")
    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "messages": [{"type": "text", "text": text}]
    }
    res = requests.post(url, headers=headers, json=payload)
    print(res.status_code, res.text)