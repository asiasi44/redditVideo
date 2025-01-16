from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Step 1: Define the range of your audio files and folder (if needed)
def combineAudio(numberOfSentences):
    audio_files = [f"audio/sentence{i}.mp3" for i in range(numberOfSentences)]  # Adjust the range if needed

    # Step 2: Load all the audio files as AudioFileClip objects
    audio_clips = [AudioFileClip(file) for file in audio_files]

    # Step 3: Concatenate the audio files
    final_audio = concatenate_audioclips(audio_clips)

    # Step 4: Write the output to a single file
    final_audio.write_audiofile("combined_output.mp3")

    # Close clips to release resources
    for clip in audio_clips:
        clip.close()