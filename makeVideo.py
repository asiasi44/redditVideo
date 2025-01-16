import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def text_update(frame_, getSentences, fps):
    for idx, sentence in enumerate(getSentences):
        if frame_ < (sentence["endTime"] * fps):
            return sentence["description"]
    return False

def makeVideo(output):
    cap = cv2.VideoCapture('calmingVideo.mp4')
    if not cap.isOpened():
        raise FileNotFoundError("The video file 'calmingVideo.mp4' could not be opened.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    output_file = 'savedVideo.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
    
    font_path = "Koblenz-Serial-Heavy.ttf"
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font file '{font_path}' not found.")
    font_size = 150
    custom_font = ImageFont.truetype(font_path, font_size)
    
    frame_ = 0
    text_active = True  # To track if text is still available
    after_false_counter = 0
    buffer_frames = int(2 * fps)  # 2 seconds buffer
    
    while text_active:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart the video
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Apply stronger Gaussian Blur (increase kernel size for more blur)
            blurred_frame = cv2.GaussianBlur(frame, (51, 51), 0)  # Adjust (35, 35) for stronger blur effect

            frameText = text_update(frame_=frame_, getSentences=output, fps=fps)
            if frameText:
                frame_pil = Image.fromarray(cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(frame_pil)

                text_bbox = custom_font.getbbox(frameText)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                x = (frame_width - text_width) // 2
                y = (frame_height - text_height) // 2

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

                blurred_frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
            else:
                if after_false_counter < buffer_frames:
                    after_false_counter += 1
                else:
                    text_active = False  # No more text, exit main loop
                    break
            
            frame_ += 1
            out.write(blurred_frame)  # Save the frame
            cv2.imshow('video', blurred_frame)  # Show the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                text_active = False  # Allow exiting the loop manually
                break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
