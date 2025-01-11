import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def text_update(frame_, getSentences, fps, questionTime, question):
    for idx, sentence in enumerate(getSentences):
        if frame_ < (questionTime * fps):
            return ""
        elif frame_ < (sentence["endTime"] * fps):
            return sentence["description"]
    return False

def makeVideo(output, question, questionTime):
    print(question, questionTime)
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
    font_path = "Koblenz-Serial-Heavy.ttf"  # Replace with the path to your font file
    font_size = 120  # Adjust based on the resolution of your video
    custom_font = ImageFont.truetype(font_path, font_size)

    # Load the intro image
    reddit_intro_image = cv2.imread('redditIntroImage.png')

    # Resize intro image to half the width and height of the video frame
    new_width = frame_width // 2
    new_height = frame_height // 2
    resized_intro_image = cv2.resize(reddit_intro_image, (new_width, new_height))

    # Calculate position to center the resized image
    x_offset = (frame_width - new_width) // 2
    y_offset = (frame_height - new_height) // 2

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if the video ends

        if frame_ < (questionTime * fps):
            # Overlay the resized intro image on the video frame
            overlay = frame.copy()
            overlay[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_intro_image
            # Blend the frame and the overlay for smooth overlay
            alpha = 1  # Adjust transparency
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
        else:
            frameText = text_update(frame_=frame_, getSentences=output, fps=fps, questionTime=questionTime, question=question)

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
                stroke_width = 12
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

