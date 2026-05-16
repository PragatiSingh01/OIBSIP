import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

engine.setProperty('rate', 160)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            return command.lower()

        except:
            print("Could not understand")
            return ""



speak("Hello, I am your voice assistant")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello, how are you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "bye" in command or "stop" in command or "exit" in command:
        speak("Goodbye")
        break