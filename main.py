import requests

api = "https://discord.com/api/v10/users/@me"
token = "bot token"

def change_bot_pfp_to(data_uri):
    response = requests.patch(url=api, headers={"Authorization": f"Bot {token}"}, json={"avatar": f"{data_uri}"})
    print(response.json())

with open("data_uri.txt", "r") as file:
    change_bot_pfp_to(file.read())