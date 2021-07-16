import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def birthdaywish():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    if day==25 and month ==8:
        speak("It is your birthday")
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir!")
    elif hour>=12 and hour<=17:
        speak("good afternoon sir!")
    elif hour>=18 and hour <=20:
        speak("good evening sir!")
    else:
        speak("good night sir!")
    speak("Hello sir!. I am friday . please sir tell me how can i help you")
def yourself():
    speak("My name is friday and my name was taken from the character of marvel comics  , who is workning for ironman aka Tony stark after the death of jarvis . I was created by kandarp sharda on may 22 ")
def takecommand():
    # takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening.........")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try :
        print("recognizing.....")
        query = r.recognize_google(audio , language="en-in")
        print(f"User said :{query}\n")
    except Exception as e:
        speak("Say that again please!")
        speak("We can not recognize your voice perfectly")
        return "None"
    return query
def sendEmail(to,content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server .ehlo()
    server.starttls()
    server.login("009kandarp@gmail.com","mukesh@sharda")
    server.sendmail("009kandarp@gmail.com",to,content)
    server.close()
def start():
    wishme()

    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipidea.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 4)
            speak("According to thw wikipidea")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google " in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = r'C:\Users\ksharda\Music\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "what time it is" in query:
            strTime = datetime.datetime.now().strftime("%H:%M%S")
            speak(f"Sir the time is {strTime}")
        elif "open picture" in query:
            speak("Wait sir , your directory is opening")
            path = r"C:\Users\ksharda\Videos\Captures"
            os.startfile(path)
        elif "stop" in query:
            speak("Your Friday machine is going to sleep")
            break
        elif "send email to raj" in query:
            try :
                speak("What should i say,Sir")
                content  = takecommand()
                to = "009kandarp@gmail.com"
                sendEmail(to,content)
                speak ("Email has been sent sir")
            except  Exception as e:
                print(e)
                speak("Sir Email has not been send due to some error")
        elif "tell me about yourself" in query:
            yourself()


start()

