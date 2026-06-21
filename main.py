import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import webbrowser


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    
# speak("Hello Yash, I am your assistant. How can I help you?")

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

    except Exception as e:
        print("Say that again please...")
        return None
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Yash! I am your assistant. How can I help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Yash! I am your assistant. How can I help you?")
    else:
        speak("Good Evening Yash! I am your assistant. How can I help you?")

wishMe()

while True:
    query = takeCommand().lower()
    if 'hello' in query:
        speak("Hello Yash, How are you?")
    elif 'how are you' in query:
        speak("I am fine, thank you. How can I assist you today?")
    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye Yash, have a great day!")
        break
    else:
        speak("I am sorry, I didn't understand that. Can you please repeat?")
