import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import getpass
import tkinter as tk
from tkinter import filedialog, Text
import os




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save('your location')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
      #put pardon me here!!!
        speak(" ")
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

    
    speak('I am Mary, Please tell me how I may be of help to you SIR?')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@gmail.com', 'password')
    server.sendmail('secondEmail@gmail.com', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

def battery():
    battery = psutil.sensors_battery()
    if "battery" in query:
        speak("battery is at")
        speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def screenshot():
    img = pyautogui.screenshot()
    img.save('Preferred location')
    speak("Screenshot taken")


if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = 'path to your browser on computer'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'path to your browser on computer'
        
        
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif "story" in query:
            speak("I have cinderella, Shrek, Fiona and Snow white, Which one should i read please?")
        elif 'cinderella' in query:
            speak("Cinderella, The story of “Cinderella” follows the fortunes of young Ella whose merchant father remarries following the death of her mother")
        elif "shrek" in query:
            speak("an ugly creature finding love  ") 
        elif "fiona" in query:
            speak("Fiona, Another beautiful story from the begining of time ")
        elif "snow white" in query:
            speak("Snow white, a beautiful princess who needs a true love kiss to survive")      

        elif "weather" in query:
            weather()
        elif "rain" in query:
            speak("I doubt it will rain today based on the wether updates sir.")
        elif "mary" in query:
            speak("Yes Sir, at your service")

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        if "are you there" in query:
                speak("Yes Sir, at your service")

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'cpu' in query:
            cpu()

        elif 'battery' in query:
            battery()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            speak("I have Omar, Black Sheriff and Kwesi Arthur , which one should i play please?")
        elif "omar" in query:
            os.startfile("Your music path")
        elif "arthur" in query:
            os.startfile("Your music path")
        elif "black" in query:
            os.startfile("Your music path")
        elif "any music" in query:
            os.startfile("Your music path")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search google' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'direction' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location for ' + location)

        elif 'created' in query:
            if platform == "win32" or "darwin":
                speak('I was created as a Digital Signal Project')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'want' in query:
            speak('All we want is an A plus so Sir Please Give us an A plus, we beg you.')
        

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com')

        elif 'notes' in query:
            speak("what should i write please?")
            rememberMessage = takeCommand()
            speak("I am saving "+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'memory' in query:
            remember = open('data.txt', 'r')
            speak("I saved " + remember.read())

        elif 'goodbye' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('What do you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'send email' in query:
            try:
                speak('What should I send?')
                content = takeCommand()
                to = 'Receipient@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')


        
            except Exception as e:
                speak('Sorry sir, Not able to send email at the moment')

        elif 'open website' in query:
            try:
                speak('What website please?')
                content = takeCommand()
                webbrowser.get('chrome').open_new_tab( 'https://'+content+"'.com'")
                speak(content + " has been opened please")

            except Exception as e:
                speak('Sorry sir, No Internet service')
