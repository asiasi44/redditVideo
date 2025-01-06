from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def combineAudioAndVideo(videoFileName, audioFileName, outputfileName):
    title = outputfileName
        # Open the video and audio
    try:
        video_clip = VideoFileClip(videoFileName + ".mp4")
        audio_clip = AudioFileClip(audioFileName + ".mp3")

        final_clip = video_clip.set_audio(audio_clip)

        final_clip.write_videofile(title + ".mp4")

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def editTheVideo(outputPath):
        # Open the video and audio
    try:
        introWithAudio = VideoFileClip("intro_with_audio.mp4")
        restOfVideo = VideoFileClip("combinedVideo.mp4")


        final_video_clip = concatenate_videoclips([introWithAudio, restOfVideo], method='compose')

        final_video_clip.write_videofile(outputPath, audio=True)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
