import speech_recognition as sr 
from time import ctime
import time
import os
from gtts import gTTS
import requests, json


def listen () :
    r = sr.recognizer()
    with sr.Microphone() as source:
        print("I am listening sir...")
        audio = r.listen(source)
    data = ""
    
    try :
        data = r.recognize_google(audio)
        print ("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")

def digital_assistant(data) :
    if "How are you today" in data:
        listening = True
        respond("I am doing very well sir, hope you are doing the same.")
    
    if "what is the time now" in data:
        listening = True
        respond(ctime())

    if "identify your self" or "who are you" in data:
        listening = True
        respond("Hello there. my name is ELSA. i am an artificial virtual interface assistanst, created by mr.vishwa. i am functioning as a virtual assistant to keep you in order, and i will help you to make your day more productive. ELSA stands for e-communication language serving assistance. thank you..")

    if "what is arkweb" in data:
        listening = True
        respond("arkweb is a blockchain based gamin platform founded by mr.vishwa gw.arkweb is runinng on it's own ark blockchain and it's native crypto token, v-coin. primary goal of arkweb is to revolutionize the future of blockchain and gaming industries.")

    if "what is skyweb" in data:
        listening = True
        respond("skyweb is commercial space exploration start-up company. skyweb is focusing on sustainable spae transportation between earth and other space object. skyweb is currently focusing on destinations, moon and mars.")

    if "who is vishwa" in data:
        listening = True
        respond("Mr. vishwa gw is an entrepenuer and founder of two start-ups arkweb and skyweb. he is currently 24 years old and living in australia. but he is a sri lankan citizen.")

    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening


