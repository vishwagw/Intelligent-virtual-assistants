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

def google_search(command):
    reg_ex = re.search('search google for (.*)', command)
    search_for = command.split("for", 1)[1]
    url = 'https://wwww.google.com/'
    if reg_ex:
        subgoogle = reg_ex.group(1)
        url = url + 'r/' + subgoogle
    speak('sure sir!')
    speak(f'searching for {subgoogle}')
    driver = webdriver.Chrome(executable_path ='driver/chromedriver.exe')
    driver.get('https://www.google.com')
    search = driver.find_element_by_name('g')
    search.send_keys(str(search_for))
    search.send_keys(Keys.RETURN)
