from ast import main
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
#print(voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir")
    speak("I am Bahadur. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)
        print("Please repeat")
        return "None"

    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open Chrome' in query:
            chromepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome"
            os.startfile(chromepath)
        
        elif 'open mail' in query:
            mailPath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\outlook"
            os.startfile(mailPath)
            
        elif ('quit' or 'bye bahadur' or 'bye') in query:
            quit()

        
