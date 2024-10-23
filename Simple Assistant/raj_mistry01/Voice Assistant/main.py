import pyttsx3
import wmi
import speech_recognition as sr
import datetime
import wolframalpha
import subprocess as sp
import time
import pyautogui 
import webbrowser as web
import random
import imdb
import psutil
import requests
import wikipedia
import pywhatkit
import smtplib
import sys
import keyboard
import speedtest
import cv2
import os
import numpy as np
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[0].id)
runnigprocesslist = []
f = wmi.WMI()
flag = 0 
def speak(audio) :
    print("Jarvis : ",end="")
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening ...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold =1 
        audio = r.listen(source,phrase_time_limit=5)
    try :
        print("Recongnizing ..")
        text = r.recognize_google(audio,language = "en-in")
        print("User said : "+text)
    except Exception as e :
        print("Say that again : ")
        return "none"
    return text
def startlistening():
    print("Started Listening : ")

def pauseListening() :
    print("Paused Listening :")

def weatherforecast(city) :
    apiKey = "apiKey"
    res = requests.get(f"openWeatherApiEndpoint").json()
    weather_ = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather_,temp,feels_like

def wish() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12 :
        speak("Good morning :")
    elif hour > 12 and hour <= 18 :
        speak("Good afternoon :")
    else :
        speak("Good evening : ")
    speak("I am jarvis ,sir  how can I assist you?")
# def sendEmail(to,content) :
#     server = smtplib.SMTP("smtp.gmail.com",587)
#     server.ehlo()
#     server.starttls()
#     server.login("emailId","yourpswd")
#     server.sendmail("emailId","toemail")
#     server.close()
if __name__ == "__main__" :
    wish()
    def main() :
        global runnigprocesslist
        tries = 0
        query = ""
        flag_ = 0
        flagForText = 0
        while True:
            if tries < 3 :
                if flag_ == 0 : 
                    query = takecommand().lower()
                    tries += 1
                else :
                    if flagForText == 1: 
                        query  = input("(Prees V + Enter to turn voice chat again)Enter your query in text : ")
                        if query == "V" :
                            flag_  = 0
                            flagForText = 0
                            pass
                        else :
                            pass
                    else : 
                        flag_ = 0
                        pass
                if "stop listening" in query :
                    pauseListening()
                    speak("Press ctrl+alt+k to continue listening.")
                    break
                elif "open notepad" in query :
                    tries = 0
                    path = "" # path to notepad
                    speak("Opening NOtepad sir.")
                    os.startfile(path)
                elif "close notepad" in query :
                    tries = 0
                    for process in f.Win32_Process() :
                        runnigprocesslist.append(process.Name)
                    if "Notepad.exe" in runnigprocesslist :
                        speak("Closing the notepad.")
                        os.system("taskkill /f /im notepad.exe")
                        flag = 1 
                        runnigprocesslist = []
                    else :
                        speak("Notepad is not opened.")
                elif "stop listening" in query :
                    tries = 0
                    speak("Press ctrl+alt+p to pause the listening")
                elif "how are you jarvis" in query :
                    tries = 0
                    speak("I am fine sir , What about you ?? Sir.")
                    query = takecommand().lower()
                    if "not feeling good" or "sad" or "bad day" in query :
                        speak("What happend sir ,Please Tell me , May I help you ?")
                        query =  takecommand().lower()
                        if "disease" in query :
                            query = query.replace(query,"drreddys.com",1)
                            path = "" # path to chrome
                            web.register("chrome",None,web.BackgroundBrowser(path))
                            web.get("chrome").open_new(query)
                        else :
                            pass
                    elif "good" or "feeling happy" in query :
                        speak("Ok sir , It seems to be nice to hear.")
                elif "open command prompt" in query :
                    tries = 0
                    speak("Opening the command propmpt.")
                    os.system("start cmd")
                elif "close command prompt" in query :
                    tries = 0 
                    for process in f.Win32_Process() :
                        runnigprocesslist.append(process.Name)
                    if "cmd.exe" in runnigprocesslist :
                        speak("Closing the command propmt.")
                        os.system("taskkill /f /im cmd.exe")
                        flag = 1 
                        runnigprocesslist = []
                    else :
                        speak("CMD is not opened.")
                    pass
                elif "clear the chat" in query :
                    tries = 0
                    os.system("cls")
                elif "are you forget to wish me" in query or "Wish me again" in query :
                    tries = 0
                    wish()
                elif "open Webcamera" in query :
                    tries = 0
                    cap = cv2.VideoCapture(0)
                    while True :
                        ret , img = cap.read()
                        cv2.imshow("webcam",img)
                        k = cv2.waitKey(50)
                        if k == 27 :
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif "open camera" in query :
                    tries = 0
                    speak("Opening Camera sir")
                    sp.run("start microsoft.windows.camera:",shell= True)
                elif "close camera" in query :
                    tries = 0
                    for process in f.Win32_Process() :
                        runnigprocesslist.append(process.Name)
                    if "WindowsCamera.exe" in runnigprocesslist :
                        speak("Closing the camera.")
                        flag = 1 
                        os.system("taskkill /f /im WindowsCamera.exe")
                        runnigprocesslist = []
                    else :
                        speak("Camera is not opened.")
                elif "calculate" in query :
                    # api = "apiKey"
                    client = wolframalpha.Client(api)
                    query = takecommand().lower()
                    ind  = query.split().index("calculate")
                    text = query.split()[ind+1:]
                    result = client.query(" ".join(text))
                    try :
                        ans = next(result.results).text
                        speak("The answer is " + ans)
                    except StopIteration :
                        speak("I could not find it , Please say it again.")
                elif "ip address" in query :
                    tries = 0
                    ip = requests.get("apiKeyOfipyfyConfig").json()
                    speak("Your Ip address is : " + ip["ip"])
                elif "wikipedia" in query :
                    tries = 0
                    speak("Searching in the wikipedia")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=2)
                    speak("According to wikipedia ")
                    speak(results)
                    print(results)
                elif "open visual code" in query :
                    tries = 0
                    path = "" # path to Vscode.exe
                    os.startfile(path)
                elif "weather report" in query :
                    tries = 0
                    ipAdd = requests.get("apiKeyOfipyfyConfig").json()
                    ipnum = ipAdd["ip"]
                    city = requests.get(f"apiKeyOfipyfyConfigEndpoint").text
                    weather , temp , feels_like = weatherforecast(city)
                    speak(f"The weather report talks about {weather}.")
                    speak(f"The temparature is {temp} kelvin.")
                    speak(f"It feels like {feels_like} kelvin.")
                elif "weather of my city" in query :
                    tries = 0
                    speak("Sir tell me your city name : ")
                    city  =  input("Enter the name of your city : ")
                    speak(f"Getting the weather of {city} : ")
                    weather , temp , feels_like = weatherforecast(city)
                    speak(f"The weather report talks about {weather}.")
                    speak(f"The temparature is {temp} kelvin.")
                    speak(f"It feels like {feels_like} kelvin.")
                elif ".com" in query:
                    tries = 0
                    path = "" # path to chrome
                    web.register("chrome",None,web.BackgroundBrowser(path))
                    web.get("chrome").open_new(query)
                elif "movie" in query :
                    movieDb = imdb.IMDb()
                    speak("Input the name of movie in text")
                    movieName = input("Enter the name : ")
                    movies = movieDb.search_movie(movieName)
                    speak("Searching for... " + movieName)
                    speak("I found these")
                    for movie in movies :
                        title = movie["title"]
                        year = movie["year"]
                        info = movie.getID()
                        movieInfo = movieDb.get_movie(info)
                        rating = movieInfo["rating"]
                        cast = movieInfo["cast"]
                        actor = cast[0:5]
                        plot = movieInfo.get('plot outline','plot summary not available')
                        speak(f"{title} movie in {year} has an imdb rating of {rating}.")
                        speak(f"It has a cast of {actor} . The plot of the movie is {plot}. ")
                # elif "send message" in query:
                #     tries = 0
                #     pywhatkit.sendwhatmsg("tosendPhoneNum","Hi raj",2,25)
                # elif "email" in query :
                #     tries = 0
                #     try :
                #         speak("What should i say")
                #         content = takecommand().lower()
                #         to = "toEmailId"
                #         sendEmail(to,content)
                #     except Exception as e :
                #         print(e)
                elif "how much battery is left" in query or "power is left" in query or "battery" in query : 
                    tries = 0
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Sir your computer system has left {percentage}% battery power.")
                    if percentage <= 15 : 
                        speak("Sir you should plug in charger.")
                    elif percentage >=15 and percentage <= 35 :
                        speak("Sir it is enough power to run on , but it is advisable to turn on battery saver made.")
                        speak("Sir Would you like to turn on battery saver mode?")
                        query = takecommand().lower()
                        if "yes" in query : 
                            pyautogui.press("win+A")
                        else : 
                            pass
                    elif percentage >= 35 and percentage <= 60 :
                        speak("Sir you should we have enough battery power.") 
                elif "turn on chat mode" in query or "chat mode" in query or "chat" in query:
                    tries = 0
                    flag_ = 1
                    flagForText = 1
                elif "subscribe the coder" in query or "subscribe" in query:
                    tries = 0
                    speak("Whoever using this my created basic voice assistant jarvis , I am thankful , Subscribe to my channel")
                    speak("Firstly go to Youtube")
                    path = "pathtoChrome``" # path to chrome
                    web.register("chrome",None,web.BackgroundBrowser(path))
                    web.get("chrome").open_new("https://www.youtube.com/")
                    speak("Click on the search bar")
                    pyautogui.moveTo(517,78,1)
                    pyautogui.click(x=517,y=78,clicks=1,interval=0,button='left')
                    speak("raj_mistry01 is username.")
                    pyautogui.typewrite("https://www.youtube.com/@raj_mistry01",0.1)
                    time.sleep(1)
                    speak("Press Enter")
                    pyautogui.press("enter")
                    speak("Here you will subscribe the channel.")
                    pyautogui.moveTo(718,602,1)
                    speak("Click here to subcribe")
                    pyautogui.click(x=718,y=602,clicks=1,interval=0,button='left')
                    speak("Thank you for the subscribing Me🙏")
                elif "volume up" in query : 
                    tries = 0
                    pyautogui.press("volumeup")
                elif "volume down" in query : 
                    tries = 0
                    pyautogui.press("volumedown")
                elif "mute the volume" in query : 
                    tries = 0
                    pyautogui.press("volumemute")
                elif "turn on the volume" in query :
                    tries = 0
                    pyautogui.press("volumemute")
                elif "minimise the window" in query: 
                    tries = 0
                    pyautogui.moveTo(1774,32,2)
                    pyautogui.click(1774,32)
                elif "maximize the window" in query  :
                    tries = 0
                    pyautogui.moveTo(763,1054,2)
                    pyautogui.click(763,1054)
                elif "internet speed" in query : 
                    tries = 0 
                    st = speedtest.Speedtest()
                    download = st.download()
                    up = st.upload()
                    speak(f"Sir we have {download} bits downloading speed per second and {up} bits downloading speed per second.")
                elif "no query thanks" in query :
                    tries = 0
                    speak("Thanks for using me sir , have a good day.")
                    sys.exit()
                elif "alarm" in query or "set alarm" in query :
                    pass
                speak("Sir do you have any other work : ")
            else :
                speak("Sir I am unable to recognize the speech.")
                speak("Sir it is better to write query in text.")
                query = input("Enter the query : ")
                query = query.lower()
                tries = 0
                flag_ = 1 
                flagForText = 0 
main()