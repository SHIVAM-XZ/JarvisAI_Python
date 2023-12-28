import datetime
import win32com.client
import speech_recognition as sr
import webbrowser
import wikipedia
import os

speaker = win32com.client.Dispatch("SAPI.Spvoice")
speaker.speak('hello i am jarvis AI')
def speak(audio):
    speaker.speak(audio)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir. I am here to help you")    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except:
        print("Say that again please...")
        return "None"
    return query
wishMe()

query = takeCommand().lower()
if "how are you" in query:
    speak("I'm fine sir, how can i help you ?")

elif "who are you" in query:
    speak("Sir I am Jarvis personal assistant ")

elif 'wikipedia' in query:
    speak('Searching Wikipedia...please wait')
    query = query.replace("wikipedia", "")
    results =  wikipedia.summary(query, sentences = 2)
    speak("wikipedia says")
    print(results)
    speak(results)

elif'open youtube' in query:
    speak("opening youtube")
    webbrowser.open("youtube.com")

elif 'open google' in query:
    speak("opening google")
    webbrowser.open('https://www.google.co.in/')

elif 'open stackoverflow' in query:
    speak("opening stackoverflow")
    webbrowser.open('https://stackoverflow.com/')

elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")
# speak(query)
  
  
songs = [["Baarish Lete Aana","D:\\Music\\Baarish Lete Aana - Darshan Raval.mp3"],
           ["Chain","D:\\Music\\Chain Sanu Ik Pal Chain.mp3"],
           ["Channa Mereya","D:\\Music\\Channa Mereya-(DJPunjab).mp3"],
           ["CHANNA VE","D:\\Music\\CHANNA VE REVIBE  AKHIL SACHDEVA  Bhoot - Part One_ The Haunted Ship  Vicky K & Bhumi P.mp3"],
           ["Jaan Ban Gaye","D:\\Music\\Jaan Ban Gaye - Khuda Haafiz.mp3"],
           ["Ghost","D:\\Music\\Justin Bieber - Ghost.mp3"],
           ["golden hour","D:\\Music\\JVKE - golden hour (@shirleysetia Remix) (Indian version).mp3"],
           ["Lambiya Judaiya","D:\\Music\\Lambiya Judaiyan Bilal Saeed 128 Kbps.mp3"],
           ["Madhanya","D:\\Music\\Madhanya_192(PaglaSongs).mp3"],
           ["Mere Liye","D:\\Music\\Mere Liye Broken But Beautiful Season 3 128 Kbps.mp3"],
           ["Satranga","D:\\Music\\Satranga Animal 320 Kbps.mp3"],
           ["Soch","D:\\Music\\Soch Harrdy Sandhu 128 Kbps.mp3"],
           ["Tujhe Kitna Chahein Aur","D:\\Music\\Tujhe Kitna Chahein Aur Acoustic Jubin Nautiyal 128 Kbps.mp3"],
           ["Yaarr Ni Milyaa","D:\\Music\\Yaarr Ni Milyaa - Hardy Sandhu 190Kbps.mp3"]]
for song in songs:
     if f"play {song[0]}".lower() in query.lower():
        speak(f"playing {song[0]}")
        os.startfile(os.path.join(song[1]))