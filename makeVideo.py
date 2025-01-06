import cv2

def text_update(frame_, getSentences, fps):
    for idx, sentence in enumerate(getSentences):
        if (frame_) < (sentence["endTime"] * fps):
            return sentence["description"]
        else:
            text = "no text found"
    return False

def makeVideo(output):
    frame_ = 0
    # Printing the result
    cap = cv2.VideoCapture('minecraftVideo.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(type(frame_width), frame_height)
    # Define the codec and create a VideoWriter object
    output_file = 'savedVideo.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 files
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    while(True):
        ret, frame = cap.read()

        font = cv2.FONT_HERSHEY_SIMPLEX

        frameText = text_update(frame_ = frame_, getSentences=output, fps=fps)

        if (frameText):
            thickness = 18
            font_scale = 4
            font_color = (255, 255, 255)
            text_size = cv2.getTextSize(frameText, font, font_scale, thickness)
            text_width, text_height = text_size[0]
            baseline = text_size[1]  # Baseline offset
            
            # Calculate the center position
            x = int((frame_width - text_width) / 2)
            y = int((frame_height + text_height) / 2) - baseline
            # Draw border text (stroke) by rendering the same text in a contrasting color multiple times
            stroke_color = (0, 0, 0)  # Black border
            for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-3, -3), (3, -3), (-3, 3), (3, 3)]:
                cv2.putText(
                    frame,
                    frameText,
                    (x + dx, y + dy),
                    font,
                    font_scale,  # Font scale
                    stroke_color,
                    thickness,  # Border thickness
                    cv2.LINE_4,
                )

            cv2.putText(frame,  
                    frameText,
                    (x, y),  
                    font, font_scale,  
                    font_color,
                    thickness,
                    cv2.LINE_4) 
        else:
            break

        frame_ = frame_ + 1
            # Display the resulting frame 
        cv2.imshow('video', frame) 
    
        # creating 'q' as the quit  
        # button for the video 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

        out.write(frame)
    
    # release the cap object 
    cap.release() 
    # close all windows 
    cv2.destroyAllWindows()