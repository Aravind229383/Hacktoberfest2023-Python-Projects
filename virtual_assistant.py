pip install SpeechRecognition gTTS pyttsx3 pywhatkit wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        pass

# Main loop for the virtual assistant
while True:
    command = take_command()
    
    if "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)
    
    elif "search" in command:
        search_query = command.replace("search", "")
        speak("Searching " + search_query)
        pywhatkit.search(search_query)
    
    elif "tell me about" in command:
        search_query = command.replace("tell me about", "")
        info = wikipedia.summary(search_query, 1)
        speak(info)
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + time)
    
    elif "exit" in command:
        speak("Goodbye!")
        break
