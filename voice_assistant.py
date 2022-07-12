from http import server
import sys
import pyttsx3 # This module used for text to speech conversion.
# pip install pyttsx3
import datetime as dt
import speech_recognition as sr
# pip install SpeechRecognition
import wikipedia # This module used to search query on wekipedia.
# pip install wikipedia
import webbrowser
import os
import smtplib

print("Activating Voice Engine Please wait...")
error_message = "Something went wrong..."
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id,'Male Voice \n\n',voices[1].id,'Female Voice')
engine.setProperty('voice',voices[0].id) #Set to female voice.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Good Morning!")
    
    elif hour>=12 and hour< 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your voice assistant sir. Please tell me how may I help you ?")

def takecommand():
    # Created this function to take microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       print("Recognizing...")
       query = r.recognize_google(audio, language = "en-in")
       print(f"User said :  {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(cc, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your-password')
    server.sendmail('your_email@gmail.com', cc, body)
    server.close()


if __name__ == "__main__":

    greet()

    while True:

        query = takecommand().lower()
        # Logic for excuting tasks based on query.

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            print(results)
            speak("According to wikipedia", results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open github' in query:
            webbrowser.open('github.com')
        
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'play music' in query:
            # Directory of your music files.
            music_dir = "path to the music directory"
            songs = os.listdir(music_dir)
            speak("This is what I found in your music directory :")
            print(songs)
            print(len(songs))
            os.startfile(os.path.join(music_dir, songs[0]))
            # add functionality of random music picking

        elif 'the time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "Path to the vs-code program file"
            os.startfile(codePath)
        
        elif 'email to' in query:
            try:
                speak("What should I say ?")
                body = takecommand()
                print(body)
                speak("To whom ?")
                cc = takecommand()
                print(cc)
                sendEmail(cc,body)
                speak("Email has been sent...")

            except Exception as e:
                print(e)
                print(error_message)
                speak(error_message)

        elif 'go to sleep' in query :
            
            print("Quitting sir. Have a good day.")
            speak("Quitting sir. Have a good day.")
            sys.exit()
