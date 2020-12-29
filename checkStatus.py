import requests

def check(transcriptID, API_token):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptID

    headers = {
        "authorization": API_token,
    }

    response = requests.get(endpoint, headers=headers)
    return response.json()["status"]