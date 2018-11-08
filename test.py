import requests
import random
from time import sleep
from array import array

URL = "https://api.telegram.org/bot628485989:AAHVFGFqkqhkevxWRHzAK0y6q9lKizpWWok/"



def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(URL + 'sendMessage', data=params)
    return response


def answer():
    array = ["Don't touch me", "I hate You", "I say Don't touch me", "What did you want?", "...", "Don't...", "Kill me Pls"]
    x = random.choice(array)
    return x

def main():  
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(URL))), answer())
            update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()

