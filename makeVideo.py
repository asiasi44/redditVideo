import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def text_update(frame_, getSentences, fps):
    for idx, sentence in enumerate(getSentences):
        if frame_ < (sentence["endTime"] * fps):
            return sentence["description"]
    return False  # No text left to display

def makeVideo(output):
    frame_ = 0
    cap = cv2.VideoCapture('minecraftVideo.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    output_file = 'savedVideo.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 files
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    # Load a custom font using Pillow
    font_path = "C:/Users/Shreejal1/Desktop/reddit_videos/redditVideo/Reddit_Sans/RedditSans-VariableFont_wght.ttf"  # Replace with the path to your font file
    font_size = 40  # Adjust based on the resolution of your video
    custom_font = ImageFont.truetype(font_path, font_size)

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if the video ends

        frameText = text_update(frame_=frame_, getSentences=output, fps=fps)

        if frameText:
            # Convert the OpenCV frame (BGR) to a Pillow Image (RGB)
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(frame_pil)

            # Calculate text size using getbbox
            text_bbox = custom_font.getbbox(frameText)  # Returns (left, top, right, bottom)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            # Calculate text position
            x = (frame_width - text_width) // 2
            y = (frame_height - text_height) // 2

            # Add text with border for better readability
            stroke_width = 3
            stroke_fill = "black"
            draw.text(
                (x, y), 
                frameText, 
                font=custom_font, 
                fill="white", 
                stroke_width=stroke_width, 
                stroke_fill=stroke_fill
            )

            # Convert the Pillow Image back to OpenCV format (BGR)
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
        else:
            # If no text is left, stop processing further
            break

        frame_ += 1
        out.write(frame)

        # Display the frame (optional)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources properly
    cap.release()
    out.release()  # Save the video
    cv2.destroyAllWindows()



