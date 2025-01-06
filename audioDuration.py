from mutagen.mp3 import MP3 

# function to convert the information into 
# some readable format 

def calculate_audio_duration(fileName):
	audio = MP3(fileName + ".mp3")
	audio_info = audio.info 
	length = audio_info.length
	return length
	