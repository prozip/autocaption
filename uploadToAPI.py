import requests

filename = "convert.wav"

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 

def getUploadUrl(API_token):
    print()
    headers = {'authorization': API_token}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))

    return response.json()['upload_url']