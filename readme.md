## Auto-generate video caption


With speech to text API, Google only allows 10 MB / audio file. You can split your audio and use google API, but the transcript is received very badly. 
So I use assemblyAI which has a limited length per month instead of size per file (still better).

Script Workflow:  Video &#8594;  Audio &#8594; Text



1. ##### Video &#8594; Audio

   Using *moviepy* library to convert most of the video format.

   ```python
   clip = mp.VideoFileClip(sourceVideoPath)
   clip.audio.write_audiofile(convertVideoPath)
   
   r = sr.Recognizer()
   audio = sr.AudioFile(convertVideoPath)
   ```

   

2. ##### Audio &#8594;Text

   Using *[AssemblyAI](https://app.assemblyai.com/login/)* as speech_recognizer API

   - Create a free *AssemblyAI* account and get 5 hours of audio transcribe per month. 

   - Upload audio to API

     ```python
     headers = {'authorization': API_token}
     response = requests.post('https://api.assemblyai.com/v2/upload',
                              headers=headers,
                              data=read_file(filename))
     
     return response.upload_url
     ```

     

   - Get transcript

     ```python
     endpoint = "https://api.assemblyai.com/v2/transcript"
     json = {
         "audio_url": upload_url
     }
     
     headers = {
         "authorization": "5b20ba32be6747228a24add78507ff8b",
         "content-type": "application/json"
     }
     
     response = requests.post(endpoint, json=json, headers=headers)
     
     return response.json()['id']
     ```

     

   - Export transcript to .**Str** 

     ```python
     endpoint = "https://api.assemblyai.com/v2/transcript/" + tranScript_ID
     headers = {
         "authorization": API_token,
     }
     response = requests.get(endpoint, headers=headers)
     return response.content.decode('utf-8')
     ```

     

   