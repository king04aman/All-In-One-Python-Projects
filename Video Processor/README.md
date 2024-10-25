# Video Processing Tool

In this Python tool processes a video file by extracting short clips, applying filters and effects, and generating subtitles for each clip. The processed clips are saved as new video files along with corresponding subtitle files.

## Features

- Extracts clips of a specified duration from the input video.
- Applies image processing effects including brightness, contrast, saturation adjustments, and blurring.
- Generates simple subtitle files for each clip.

## Requirements

To run this script, you'll need the following Python packages:

- `opencv-python`
- `pysrt`

You can install these using pip:

```bash
pip install opencv-python pysrt
```

## Usage

1. **Input Video**: The script prompts you to enter the link to a YouTube video. Make sure to use a video URL that is accessible and can be downloaded.
   
2. **Clip Duration**: The default duration for each extracted clip is set to 10 seconds. You can modify this value in the script as needed.

3. **Run the Script**: Execute the script using Python:

   ```bash
   python video_processor.py
   ```

4. **Output**: 
   - The processed clips will be saved as `clip0_out.mp4`, `clip1_out.mp4`, etc.
   - Corresponding subtitle files will be saved as `clip0_subtitle.srt`, `clip1_subtitle.srt`, etc.

## Code Explanation

- **Video Capture**: The script uses OpenCV to read frames from the video.
- **Image Processing**: Each frame within the clip duration is processed using filters and effects:
  - **Brightness and Contrast**: Adjusts the brightness and contrast of the frame.
  - **Saturation**: Modifies the saturation of the frame.
  - **Blurring**: Applies Gaussian blur and combines with a weighted blend for a smoother look.
  
- **Subtitle Generation**: For each clip, a simple subtitle text ("This is a sample subtitle") is generated and saved in a `.srt` file format.

## Limitations

- The script assumes the video file can be read directly via OpenCV, which may not be applicable for all YouTube links without prior downloading.
- Subtitle text is static; you may want to customize it based on the content of each clip.

