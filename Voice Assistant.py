import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except:
            return "Sorry, could not understand."

def run_assistant():
    speak("How can I help you?")
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    else:
        speak("Command not recognized")
    

run_assistant()
