import requests

def getID(upload_url, API_token):
    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
        "audio_url": upload_url
    }

    headers = {
        "authorization": API_token,
        "content-type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)

    return response.json()['id']
