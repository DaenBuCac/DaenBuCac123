from flask import Flask, request
import requests

app = Flask(_name_)

TELEGRAM_BOT_TOKEN = "8126863127:AAE4JdN4GiDoImS11vwlmnqvgNr9tAREY2U"
CHAT_ID = "2055159900"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if not data or 'message' not in data:
        return {"status": "error", "message": "Invalid request"}, 400
    
    message = data['message']
    send_telegram_message(f"🔔 Thông báo mới: {message}")
    
    return {"status": "success", "message": "Notification sent"}, 200

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=5000)
