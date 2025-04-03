import speech_recognition as sr
import pyttsx3

from ELSA.features import date_time
from ELSA.features import launch_app
from ELSA.features import weather
from ELSA.features import website_open
from ELSA.features import wikipedia
from ELSA.features import news
from ELSA.features import send_email
from ELSA.features import google_calender
from ELSA.features import google_search
from ELSA.features import note
from ELSA.features import system_status
from ELSA.features import loc

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)
engine.setProperty('voice', voices[1].id)

class ElsaVirtualAssistantInterface():
    def __init__(self) :
        pass

    def mic_input(self):
        try:
            r = sr.Recognizer()
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
            with sr.Microphone() as source:
                print("I an Listening......")
                r.energy_threshold = 4000
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                print("Recognizing Your Voice... pleas wait...")
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
            except:
                print('Pleas try again.')
                command = self.mic_input()
            return command
        except Exception as e:
            return False
        
    def tts(self, text):
        try:
            engine.say(text)
            engine.runAndWait()
            engine.setProperty("rate", 175)
            return True
        except:
            t = "Sorry sir. I can not understand about your data input."
            print(t)
            return False
        
    def tell_me_date(self):
        return date_time.date()
    
    def tell_time(self):
        return date_time.time()
    
    def launch_any_app(self, path_of_app):
        return launch_app.launch_appp(path_of_app)
    
    def website_opener(self, domain):
        return website_open.website_opener(domain)
    
    def weather(self, city):
        try:
            res = weather.fetch_weather(city)
        except Exception as e:
            print(e)
        return res
    
    def tell_me(self, topic):
        return wikipedia.tell_me_about(topic)
    
    def news(self):
        return news.get_news()
    
    def send_mail(self, sender_email, sender_password, receiver_email, msg):
        return send_email.mail(sender_email, sender_password, receiver_email, msg)
    
    def search_anything_google(self, command):
        google_search.google_search(command) #return func?

    def take_note(self, text):
        note.note(text) #return func?

    def system_info(self):
        return system_status.system_status()
    
    def location(self, location):
        current_loc, target_loc, distance = loc.loc(location)
        return current_loc, target_loc, distance
    
    def my_location(self):
        city, state, country = loc.my_location()
        return city, state, country
    


    
        