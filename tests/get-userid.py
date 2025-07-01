import requests

from src.const import BOT_TOKEN


def get_updates():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    response = requests.get(url)
    return response.json()


def main():
    updates = get_updates()
    for update in updates['result']:
        if 'message' in update:
            user_id = update['message']['from']['id']
            user_name = update['message']['from']['first_name']
            print(f'User  ID: {user_id}, User Name: {user_name}')


if __name__ == '__main__':
    main()
