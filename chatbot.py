from utils import speak, takeCommand
from commands import *
import datetime

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. Say help to know commands.")

def show_help():
    speak("You can say commands like:")
    print("""
Open Google
Open YouTube
What is the time
What is the date
Wikipedia Coimbatore
Write note
Show notes
Set reminder
Show reminders
Exit
""")

def run_chatbot():
    wishMe()

    while True:
        try:
            query = takeCommand()

            if query == "none":
                continue

            if "open google" in query:
                open_google()

            elif "open youtube" in query:
                open_youtube()

            elif "time" in query:
                tell_time()

            elif "date" in query:
                tell_date()

            elif "wikipedia" in query:
                search_wikipedia(query)

            elif "write note" in query:
                speak("What should I write?")
                note = takeCommand()
                if note != "none":
                    write_note(note)

            elif "show note" in query or query == "show":
                show_notes()

            elif "set reminder" in query:
                speak("What reminder?")
                rem = takeCommand()
                if rem != "none":
                    set_reminder(rem)

            elif "show reminder" in query:
                show_reminders()

            elif "help" in query:
                show_help()

            elif "exit" in query or "stop" in query or "quit" in query:
                speak("Goodbye!")
                break

            elif "shutdown" in query:
                shutdown_system()

            else:
                speak("Command not recognized. Say help.")

        except KeyboardInterrupt:
            speak("Assistant stopped.")
            break

if __name__ == "__main__":
    run_chatbot()
