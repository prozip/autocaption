import requests

def export(tranScript_ID, API_token, output):
    endpoint = "https://api.assemblyai.com/v2/transcript/"+ tranScript_ID +"/srt"

    headers = {
        "authorization": API_token,
    }

    response = requests.get(endpoint, headers=headers)

    with open(output,mode ='w') as file: 
        file.write(response.content.decode('utf-8'))