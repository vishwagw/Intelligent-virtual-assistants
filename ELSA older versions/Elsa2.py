import pyttsx3 
import speech_recognition as sr 
from playsound import playsound
import random
import datetime
hour = datetime.datetime.now().strftime('%H:%M')
date = datetime.date.today().strftime('%d/%B/%Y')
date = date.split('/')
import tensorflow
import librosa
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import openpyxl
import pyaudio
import webbrowser as wb
import numpy as np 
import google
from module import command_answers
commands = command_answers.commands
answers = command_answers.answers

#print(commands[1])
#print(answers[1])


#my_name = 'ELSA'

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

def search(sentence):
    wb.get(chrome_path).open('https://www.google.com/search?q=' + sentence)

search('python')