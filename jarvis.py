import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis sir, please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("User said: ",query)
    except Exception as e:
        print("say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('vishalreddy326@gmail.com','Vishal3105')
    server.sendmail('vishalreddy326@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    
    if True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Acoording to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "play music" in query:
            music_dir="E:\\movies"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\vishal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to vishal' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="vishalreddy326@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send the email")



        

