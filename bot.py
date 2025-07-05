import time
import requests

TOKEN = "7736149860:AAEd9QqxIuO53k2KZEOqt2c7YIwP5PmB730"
URL = f"https://api.telegram.org/bot{7736149860:AAEd9QqxIuO53k2KZEOqt2c7YIwP5PmB730}/"

last_update_id = 0

def get_updates():
    global last_update_id
    response = requests.get(URL + "getUpdates", params={"offset": last_update_id + 1})
    return response.json()["result"]

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

def main():
    global last_update_id
    while True:
        updates = get_updates()
        for update in updates:
            last_update_id = update["update_id"]
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "")

            if text == "/start":
                send_message(chat_id, "Здорова, Рыжий! Чё подбираем?")
            else:
                send_message(chat_id, f"Принял: {text}")

        time.sleep(1)

if __name__ == "__main__":
    main()
