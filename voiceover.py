from pyt2s.services import stream_elements

def voiceover_function(voiceoverText, ouputFileName):
    # Default Voice
    data = stream_elements.requestTTS(voiceoverText)

    # Custom Voice
    # data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.', stream_elements.Voice.Russell.value)

    with open( ouputFileName + '.mp3', '+wb') as file:
        file.write(data)