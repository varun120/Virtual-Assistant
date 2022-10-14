from ast import Try
from email.mime import audio
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def JarvisVoice(audioinput):
    engine.say(audioinput)
    engine.runAndWait()

# JarvisVoice("Hello Friends")   

def wish():
    h = int(datetime.datetime.now().hour)
    print("Time",h)
    if h>=0 and h<12:
        JarvisVoice("Good Morning")
    elif h>=12 and h<18:
        JarvisVoice("Good Afternoon")
    else:
        JarvisVoice("Good Evening")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = 'en-in')
        print("user said : ",query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "none"
    return query  

wish()

status = True
while True:
    query=takecommand().lower()

    if "what is" in query or "who is" in query: 
        JarvisVoice("searching in wikipedia")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences = 2)
        print(result)
        JarvisVoice("According to wikipedia....")
        JarvisVoice(result)
    elif "open google" in query:
          webbrowser.open("google.com")
    elif "open gmail" in query:
          webbrowser.open("gmail.com")
    elif "open youtube" in query:
          webbrowser.open_new_tab("youtube.com")          
                
    else:
        pass        









