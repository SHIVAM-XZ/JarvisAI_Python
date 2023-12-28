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
while True:
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

#   elif 'play music'in query:
#     music_dir = "C:\\Users\\Baali\\Music"
#     songs = os.listdir(music_dir)
#     print(songs)
#     os.startfile(os.path.join(music_dir, songs[0]))

  elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")
# speak(query)
