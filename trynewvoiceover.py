import requests
import json

def generateMurfVoiceOver(voiceoverText, ouputFileName):

    url = "https://api.murf.ai/v1/speech/generate"

    payload = json.dumps({
    "voiceId": "en-US-zion",
    "style": "Promo",
    "text": voiceoverText,
    "rate": 0,
    "pitch": 0,
    "sampleRate": 48000,
    "format": "MP3",
    "channelType": "MONO",
    "pronunciationDictionary": {},
    "encodeAsBase64": False,
    "variation": 1,
    "audioDuration": 0,
    "modelVersion": "GEN2"
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'api-key': 'ap2_7dd0e743-7ec2-4ea8-a477-581bb33ff28e'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


    audio_url = response.json().get("audioFile")
    print(audio_url)
    if audio_url:
        audio_response = requests.get(audio_url)
        if audio_response.status_code == 200:
            with open(ouputFileName+".mp3", "wb") as audio_file:
                audio_file.write(audio_response.content)
            print("Audio downloaded successfully.")
        else:
            print("Failed to download audio.")