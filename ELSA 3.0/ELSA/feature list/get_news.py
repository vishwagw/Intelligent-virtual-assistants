from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 110)

