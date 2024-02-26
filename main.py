import requests
import base64
import mimetypes

def file_to_data_uri(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    base64_data = base64.b64encode(binary_data).decode('utf-8')

    # Determine the MIME type from file extension
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        mime_type = 'application/octet-stream'

    data_uri = f'data:{mime_type};base64,{base64_data}'

    return data_uri

if __name__ == "__main__":
    
    endpoint = "https://discord.com/api/v10/users/@me"
    token = f"Bot {input('Please copy and paste your bot token: ')}"
    filename = input("Please provide the path to the image you would like the bot to have: ")

    response = requests.patch(endpoint, headers={"Authorization": token}, json={"avatar": file_to_data_uri(filename)})

    if response.status_code == 200:
        print("Bots profile picture has been successfully changed!")
    else:
        print("Discord's API returned non 200 HTTP response (%s)" % response.status_code)
        print(response.text)
