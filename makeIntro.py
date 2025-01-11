import cv2
import numpy as np
from audioDuration import calculate_audio_duration
from combineAudioAndVideo import combineAudioAndVideo

def make_intro():
    # Get audio duration
    duration = calculate_audio_duration("audio/question")
    
    # Load the image
    image_path = "intro.png"
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image '{image_path}' not found.")

    # Define video properties
    height, width, _ = image.shape
    fps = 30  # Frames per second
    frame_count = int(duration * fps)

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
    video_path = "output_intro.mp4"
    video_writer = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    # Write frames to the video
    for _ in range(frame_count):
        video_writer.write(image)

    # Release the VideoWriter
    video_writer.release()
    print(f"Video saved as '{video_path}'")

    combineAudioAndVideo("output_intro", "audio/question", "intro_with_audio")
