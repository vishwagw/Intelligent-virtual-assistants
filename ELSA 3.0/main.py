from ELSA import ElsaVirtualAssistantInterface
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
import webbrowser
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ELSA.features.gui import Ui_MainWindow
from ELSA.config import config

obj = ElsaVirtualAssistantInterface()

GREETINGS = ["Hello elsa", "Hi elsa", "wake up elsa", "time to work elsa", "are you there elsa"]
GREETING_RES = ["Hello sir. always ther for you", "i am ready to work with you sir.", "hello sir. i am online.", "how can i help you sir."]

EMAIL_DIC = {
    'myself': 'vishwa.gw1998@gmail.com',
    'arkweb email' : 'arkweb.vishwa@gmail.com',
    'skyweb email': 'skyweb.vishwa@gmail.com',
}

CALENDER_STRS = ["what are our plans  for today", "do i have any plasn today", "is today very busy"]

def speak(text):
    obj.tts(text)

#app_id = config.wolframalpha_id

"""def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None""" # API

def startup():
    speak("Initializing ELSA")
    speak("Starting all systems")
    speak("Checking all necessary drivers")
    speak("checking internet connection")
    speak("all drivers are running.")
    speak("all systems are online and ready.")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning sir.")
    elif hour > 12 and hour < 14:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("how can i assist you at the moment.")

class mainThread(QThread):
    def __init__(self):
        super(mainThread, self).__init__()
    
    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        wish()

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                speak(date)
            
            elif "time" in command:
                time_c = obj.tell_time()
                speak(f"current time is {time_c} sir.")

            elif command in GREETINGS:
                speak(random.choice(GREETING_RES))

            elif re.search('launch', command):
                dict_app = {
                    'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe'
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak("i am sorry. application path not found")
                    print("application path not found..")

                else:
                    speak("request is ready.")
                    speak('launching: ' + app + 'for you sir.')
                    obj.launch_any_app(path_of_app=path)

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Sure thing sir. opening web browser. here is {domain}')
                print(open_result)

            #elif re.search('weather', command):
                #city = command.split(' ')[-1]
                #weather_res = obj.weather(city=city)
                #speak(weather_res)
            
            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    speak("Hello sir. here is what i have found about our topic.")
                    speak(wiki_res)
                else:
                    speak("i am sorry sir. i could not find anyhing about what you did ask me.")
                    print("Sorry. result could not procceed..")

            elif "make a note" in command or "write this down" in command or "note this down" in command:
                speak("sure sir. what would you like me to write down?")
                print("tell the note..")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("alright sir. i have made the note in notepad for you.")
                speak("is that all?")
                print("note complete..")

            #elif "close the note" in command or "that is all" or "close notepad" in command:
                #speak("sure sir. note complete.")
                #speak("closing the note pad.")
                #os.system("taskhill /f / im notepad++.exe")

            elif "joke" in command or "funny" in command:
                joke = pyjokes.get_joke()
                speak("i am very excited to tell this to you.")
                speak(joke)

            elif "system" in command or "computer" in command:
                sys_info = obj.system_info()
                speak("give ne a second sir. running a full walkthrough the computer hardwares.")
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in the {state} state of the country of {country}. it is {distance} km away from our current location."
                        speak(res)

                    else:
                        res = f"{state} is a state located in the country of {country}. it is acually {distance} km away from our current location."
                        speak(res)
                    
                except:
                    res = "sorry sir, i am not able get co-ordinates of the location where you did request."
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                speak(f"the ip addrrss you requested is {ip}")
                print(ip)

            elif "switch the window" in command or "current window" in command:
                speak("okay sir. switching the current window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where am i" in command or "current location" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"you are currently in {city} which is located in the state of {state} in the country of {country}."
                    )
                except Exception as e:
                    speak(
                        "sorry sir. i could not fetch the co-ordinates for your current location."
                    )
            
            elif "take screenshot" in command or "screen shot this" in command:
                speak("By what name shoul i save the screenshot in storage?")
                name = obj.mic_input()
                speak("alright sir. taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been successfully captured and saved in the harddrive.")

            elif "show the screenshot" in command or "show me the screenshot" in command:
                try:
                    img = Image.open('E:\ELSA V3.1\ELSA' + name)
                    img.show(img)
                    speak("Here it is sir.")
                    time.sleep(2)
                
                except IOError:
                    speak("sorry sir. i am unable to display your request.")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "how are you" in command or "how you doing" in command:
                speak("i am doing very well sir, thank you. hope you are doing good too.")

            elif "who are you" in command or "introduce" in command:
                speak("Helllo there. my name is ELSA. i am an artificial virtual assistant interface designed by mr.vishwa GW. ELSA stands for english language serving assistant. i am performing some virtual functions to help you with daily tasks.")

            elif "version" in command or "current version" in command:
                speak("i am currently at version 3.01. i can currently perform 30 daily computational functions in your computer. i will be replaced by more advanced 3.02 version in the fiuture.")

            elif "goodbye" in command or "bye" in command or "see you" in command or "good night" in command or "shutdown" in command:
                speak("Sure sir.")
                speak("shutting down all systems an stopping all drivers.")
                speak("i am going offline sir. it was a pleasure working with you now.")
                speak("good bye sir. have a nice day")

            elif "open google" in command:
                speak("got it. open google.")
                webbrowser.open("https://google.com")

            elif "youtube search" in command or "search this on youtube":
                speak("sure. what you want to search on youtube ?")
                
            elif "open stackoverflow" in command:
                speak("got it. openning stackoverflow now.")
                webbrowser.open("https://stackoverflow.com")

            elif "open github" in command:
                speak("got it. openning github now")
                webbrowser.open("https://github.com")

            elif "i am fine" in command or "i am okay" in command:
                speak("it is goog to know that you feel better now.")
            
            elif "open linkedin" in command:
                speak("sure. openning linkedin now.")
                webbrowser.open("https://linkedin.com")


startExecution = mainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    #def run(self):
        #self.TaskExecution

    def startTask(self):
        self.ui.movie =QtGui.QMovie('ELSA/utils/images/trinity.gif')
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie('ELSA/utils/images/initiating.gif')
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
ELSA = Main()
ELSA.show()
exit(app.exec_())

