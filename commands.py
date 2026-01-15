import wikipediaapi
import webbrowser
import datetime
import os
from utils import speak

wiki = wikipediaapi.Wikipedia(
    user_agent="VoiceAIChatbot/1.0",
    language="en"
)

def open_google():
    webbrowser.open("https://www.google.com")
    speak("Opening Google")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube")

def tell_time():
    speak("The time is " + datetime.datetime.now().strftime("%H:%M:%S"))

def tell_date():
    speak("Today's date is " + datetime.datetime.now().strftime("%d %B %Y"))

def search_wikipedia(query):
    topic = query.replace("wikipedia", "").replace("about", "").strip()

    page = wiki.page(topic)
    if page.exists():
        speak(page.summary[:500])
    else:
        speak("No information found on Wikipedia.")

def write_note(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
    speak("Note saved.")

def show_notes():
    if not os.path.exists("notes.txt"):
        speak("No notes found.")
        return

    with open("notes.txt", "r") as f:
        content = f.read().strip()

    if content:
        speak("Here are your notes.")
        print(content)
    else:
        speak("You have no notes.")

def set_reminder(text):
    with open("reminders.txt", "a") as f:
        f.write(text + "\n")
    speak("Reminder saved.")

def show_reminders():
    if not os.path.exists("reminders.txt"):
        speak("No reminders found.")
        return

    with open("reminders.txt", "r") as f:
        content = f.read().strip()

    if content:
        speak("Here are your reminders.")
        print(content)
    else:
        speak("You have no reminders.")

def shutdown_system():
    speak("Shutdown command received.")
