import requests


# API_token = "5b20ba32be6747228a24add78507ff8b"
# tranScript_ID = "xzd9luo4e-5c0a-4625-b663-7d2bac93861a"

def export(tranScript_ID, API_token, output):
    endpoint = "https://api.assemblyai.com/v2/transcript/"+ tranScript_ID +"/srt"

    headers = {
        "authorization": API_token,
    }

    response = requests.get(endpoint, headers=headers)

    with open(output,mode ='w') as file: 
        file.write(response.content.decode('utf-8'))