# libs:
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver

# engine :
engine = pyttsx3.init('sapi5')
#voice of the assistant:
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id) # 1- female and 0-male


# building the function for speeking:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greeting at start:
def greet_start():
    # get date and time 
    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(hour, Time)
    print(date, month, year)
    # start speaking:
    if hour>=0 and hour<12:
        speak("Good Morning. ")

    elif hour>=12 and hour<16:
        speak("Good Afternoon. ")

    elif hour>=16 and hour<24:
        speak("Good Evening. ")
    
    speak("Hello Mr.vishwa , welcome back.. ")
    # speak date and time:
    #speak(f"the current Time is {hour}")
    #speak(f"and the current data is {date} {month} {year}")
    
    # finishing greet:
    speak("My name is Trinity. how may i help you today?")

# greet_start()

# commands function:
def basicCommands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("I am listening..")
        query = r.recognize_google(audio, language='en')
        print(f" You said: {query}\n")

    except Exception as e:
        print(e)
        print("please speak again...")
        speak(" I am sorry. I could not understand what you said just now. Can you repeat it again, ")
        return "None"
    return query

# email responding mode:
def emailsenderMode(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youemail@gmail.com', 'username')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# initializign the program:
# starting functions:
if __name__ == "__main__":
    greet_start()
    #while loop:
    while True:
        query = basicCommands().lower()
        










