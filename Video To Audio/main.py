import moviepy
from tkinter.filedialog import *

askForVideo = askopenfilename()
video = moviepy.editor.VideoFileClip(askForVideo)

audio = video.audio
audio.write_audiofile("demo.mp3")

print("Conversion Completed !!")
