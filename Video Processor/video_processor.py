import cv2
import pysrt

# Load the input video
input_file = input("Enter the YouTube video link: ")
cap = cv2.VideoCapture(input_file)

# Set the start and end times for each short video clip
clip_duration = 10.0
clip_start_time = 0.0
clip_end_time = clip_start_time + clip_duration

# Set up OpenCV for video processing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
brightness = 30
contrast = 1.5
saturation = 1.5

# Process each short video clip
i = 0
while cap.isOpened():
    # Read the next frame from the input video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get the current time in seconds
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
    
    # If the current time is within the current clip, process the frame
    if current_time >= clip_start_time and current_time <= clip_end_time:
        # Apply the filters and effects
        frame = cv2.filter2D(frame, -1, kernel)
        frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(frame)
        s = cv2.convertScaleAbs(s, alpha=saturation, beta=0)
        frame = cv2.merge((h, s, v))
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        frame = cv2.GaussianBlur(frame, (5,5), 0)
        frame = cv2.addWeighted(frame, 1.5, cv2.blur(frame, (10,10)), -0.5, 0)
        
        # Write the modified frame to a new video file
        out = cv2.VideoWriter('clip' + str(i) + '_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        out.write(frame)
        out.release()
        
        # Generate subtitles for the clip
        subtitle_text = "This is a sample subtitle"
        subtitle_duration = clip_duration
        subtitle_file = pysrt.SubRipFile()
        subtitle = pysrt.SubRipItem(index=1, start=0, end=subtitle_duration, text=subtitle_text)
        subtitle_file.append(subtitle)
        subtitle_file.save('clip' + str(i) + '_subtitle.srt')
        
        # Move to the next clip
        i += 1
        clip_start_time += clip_duration
        clip_end_time += clip_duration
    
    # If the current time is past the end of the current clip, move to the next clip
    elif current_time > clip_end_time:
        clip_start_time += clip_duration
        clip_end_time += clip_duration

# Release the resources
cap.release()
cv2.destroyAllWindows()
