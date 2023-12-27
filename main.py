import datetime
import win32com.client
import speech_recognition as sr
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
speak(query)
