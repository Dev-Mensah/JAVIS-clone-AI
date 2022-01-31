import tkinter as tk
from tkinter import filedialog, Text
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



root = tk.Tk()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
   


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

    
    speak('I am A.I. Please tell me how I may be of help to you SIR?')

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
        speak("pardon me")
        return 'None'
    return query


def addApp():
    filename= filedialog.askopenfilenames(initialdir="/", title="select file", filetype=(("executables", "*.exe"), ("all files", "*.*")))

canvas = tk.Canvas(root, height=800, width=800, bg="#263d42")
canvas.pack()


frame = tk.Frame(root, bg="#263d42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(frame, text="Open File", padx=10, pady=5, fg="blue", bg="white", command=wishMe)
openFile.place(x= 200, y = 200)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#263d42", bg="white" )
runApps.pack()
openFile.pack()

root.mainloop()