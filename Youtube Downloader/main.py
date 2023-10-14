from pytube import YouTube
import PIL
from PIL import Image
import urllib.request
print("please enter the link you wanna download from the youtube : ")
link= input()
yt= YouTube(link)
print("The title of the video is :")
print(yt.title)
vid_down = yt.streams.get_highest_resolution()
vid_down.download("QuickTube")
print("the video thumbnail is :")
thumbnail= yt.thumbnail_url
urllib.request.urlretrieve(thumbnail,"video.png")
img = Image.open("video.png")
img
