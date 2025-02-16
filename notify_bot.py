from flask import Flask, request
import requests
import os  # Import thư viện để đọc biến môi trường

app = Flask(__name__)

# Đọc TELEGRAM_BOT_TOKEN và CHAT_ID từ biến môi trường
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
        print("Lỗi: Chưa cấu hình TELEGRAM_BOT_TOKEN hoặc CHAT_ID.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        print(f"Lỗi gửi tin nhắn: {response.text}")

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if not data or 'message' not in data:
        return {"status": "error", "message": "Invalid request"}, 400
    
    message = data['message']
    send_telegram_message(f"🔔 Thông báo mới: {message}")
    
    return {"status": "success", "message": "Notification sent"}, 200

if __name__ == '_main_':  # Sửa lỗi name -> _name_
    app.run(host="0.0.0.0", port=5000)
