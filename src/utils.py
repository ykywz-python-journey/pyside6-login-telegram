import requests

from src.const import BOT_TOKEN, GROUP_ID

def check_user_in_group(user_id):
    # Get chat members list
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id={GROUP_ID}&user_id={user_id}"
    response = requests.get(url).json()

    if response.get("ok"):
        status = response["result"]["status"]
        # Possible statuses: "creator", "administrator", "member", "left", "kicked", "restricted"
        return status in ["creator", "administrator", "member"]
    return False