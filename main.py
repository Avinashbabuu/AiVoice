import speech_recognition as sr
import pyttsx3
import os
import wikipedia

# Set your assistant name (trigger word)
WAKE_WORD = "shaktimaan"

# Initialize engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='hi-IN')  # Hindi+Hinglish
        print(f"🗣️ You said: {query}")
    except:
        return ""
    return query.lower()

def process_command(command):
    if "open notepad" in command:
        os.system("notepad")
        speak("Notepad khol diya gaya hai.")
    elif "wikipedia" in command:
        speak("Wikipedia se khoj rahe hain.")
        result = wikipedia.summary(command, sentences=2)
        speak(result)
    elif "play music" in command:
        os.system("start path\\to\\music.mp3")
    else:
        speak("Maaf kijiye, mujhe samajh nahi aaya.")

# MAIN LOOP
while True:
    query = take_command()
    if WAKE_WORD in query:
        speak("Ji haan, boliye")
        command = take_command()
        process_command(command)
