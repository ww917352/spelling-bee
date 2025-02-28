import requests


def lookup(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        return response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    else:
        return None
