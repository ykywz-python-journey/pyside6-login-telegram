import requests

from src.const import BOT_TOKEN

def get_group_id():
    # Fetch latest updates to find the group chat ID
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    print(response)

    for update in response.get("result", []):
        if "message" in update and "chat" in update["message"]:
            chat = update["message"]["chat"]
            if chat["type"] == "group" or chat["type"] == "supergroup":
                print(f"Group Name: {chat.get('title', 'N/A')}")
                print(f"Group ID: {chat['id']}")


print(get_group_id())
