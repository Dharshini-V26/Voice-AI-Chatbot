import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You:", query)
        return query.lower()

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        speak("Sorry, I did not understand.")
        return "none"
