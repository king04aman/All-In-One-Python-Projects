import pyttsx3,datetime,os,random,requests
import wikipedia,webbrowser,sys,pywhatkit
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)


# To convdert text into voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
    except Exception:
        speak("Can you please say that again ... ")
        return 'none'
    return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak("Good morning Sir")
    elif hour>12 and hour<16:
        speak("Good afternoon Sir")
    elif hour>16 and hour<22:
        speak("Good evening Sir")
    speak("I am jarvis, Please tell me how can i help you !")


if __name__ == "__main__":
    wish()
    if 1:
        query = takecommand().lower()

        if 'open notepad' in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
            speak("Please wait ! While I am opening notepad for you!")

        elif "open cmd" in query:
            os.system('start cmd')
            speak("Opening Command Promte")

        elif "play music" in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
            speak("Playing Music")

        elif "ip address" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your Ip address is {ip}")

        elif 'wikipedia' in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak(f"according to wikipedia {results}")
        
        elif "open youtube" in query:
            webbrowser.open('www.youtube.com/')

        elif "open instagram" in query:
            webbrowser.open('www.instagram.com/')

        elif "open facebook" in query:
            webbrowser.open('www.facebook.com/')

        elif "open twitter" in query:
            webbrowser.open('www.twitter.com/')

        elif "open google" in query:
            speak('Sir what should i search on google ! ')
            varg = takecommand().lower()
            webbrowser.open(varg)

        # elif 'send message' in query:
        #     pywhatkit.sendwhatmsg("+919988776655",'Hello I am Jarvis ! How are you Sir ?',18,33,10,True)

        # elif 'play song on youtube' in query:
        #     speak("Which song would you like to play on youtube ? ")
        #     song = takecommand().lower()
        #     pywhatkit.playonyt(song)

        # elif 'play video' in query:
        #     speak("Which video would you like to play on youtube ? ")
        #     vsong = takecommand().lower()
        #     pywhatkit.playonyt(vsong)


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

