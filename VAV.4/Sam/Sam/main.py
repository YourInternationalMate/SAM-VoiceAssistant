# Module
import speech_recognition as sr
import os
import pyttsx3
import datetime
import warnings
from time import sleep
import wikipedia 
import subprocess
import requests
import webbrowser
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

# Funktionen

import info
#import musicplayer
import recognizer
import systemfunctions
import translatorfunction
import weather
import wiki



warnings.filterwarnings("ignore")

'''
To Do:
Stimmenerkennung
'''


def recordAudio():      # Aufnahme und Umwandlung
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        audio = r.listen(source)
    
    data = ""
    try:
        data = r.recognize_google(audio, language="de")
        print(data)
    except sr.UnknownValueError:
        print("Das habe ich leider nicht verstanden")
    except sr.RequestError as e:
        print("service error"+ e)

    return data

def assistantResponse(text):    # Response
    print(text)
    engine = pyttsx3.init('sapi5')
    engine. setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    
def wakeWord(text):     # Wake Words
    WAKE_WORDS = ["sam"]

    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
        
    return False
 
def login(url,usernameId, username, passwordId, password, submit_buttonId):     # Auf Moodle anmelden
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()


# MAIN

weatherSTR = ["grad", "wetter"]
time_str = ["wie viel uhr", "wie spät"]
date_str = ["der wievielte", "den wievielten"]
noteSTR = ["erstelle eine notiz", "erstelle eine datei", "make a note", "erstell eine notiz", "notiz erstellen"]

assistantResponse("Hallo ich bin Sam.")

while True:
    text = recordAudio()
    response = ""
    if wakeWord(text) == True:


        if "was ist" in text.lower():
            tran = translatorfunction.trans(text)
            response = response + tran
        
        
        for phrases in time_str:
            if phrases in text.lower():
                now = datetime.datetime.now()
                if now.hour < 10:
                    hour = "0" + str(now.hour)
                else:
                    hour = str(now.hour)
                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                response = response + " " + "Es ist " + str(hour) + ":" + minute +". "

    
        if "der wievielte" or "den wievielten" in text.lower():
            if phrases in text.lower():
                get_date = info.getDate() 
                response = response + "" + get_date   

        if "welcher tag" and "heute" in text.lower():
            response = response + info.getDay()
            
        for phrases in weatherSTR:
            if phrases in text.lower():
                wetter = weather.weather(text)
                wetter = str(wetter)
                user_api = "989fd048fb579d6222799cb5d1e294d9"
                complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+wetter+"&appid="+user_api
                api_link = requests.get(complete_api_link)
                api_data = api_link.json()
                temp_city = ((api_data['main']['temp']) - 273.15)
                temp_city = int(temp_city)
                temp_city = str(temp_city)
                response = response + temp_city

        if "status" in text.lower():
            statusV = info.status()
            response = response + statusV

        elif "wer ist das" in text.lower():
            systemfunctions.takeScreenshot()
            recognizer.who_is_it()
            sleep(10)
            os.remove("unknown_faces/test.jpg")

        elif "wer ist" in text.lower():
            assistantResponse("Ich suche auf Wikipedia")
            person = wiki.getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            person = wiki.getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            lang = "de"
            translator = translatorfunction.Translator(to_lang=(lang))
            wiki = translatorfunction.translate(wiki)
            assistantResponse("Laut Wikipedia")
            response = response + " " + wiki

        # elif "song" in text.lower():
        #     assistantResponse("Was willst du suchen?")
        #     search = recordAudio()           
        #     musicplayer.music(search)
            
        elif "öffne google" in text.lower():
            webbrowser.open("chrome")

        elif "öffne youtube" in text.lower():
            chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chromedir).open("http://youtube.com/")
            
        elif "öffne moodle" in text.lower():
            conf = yaml.safe_load(open("loginDetails.yml", "r"))
            myMlEmail = conf['ml_user']['email']
            myMlPassword = conf['ml_user']['password']
            driver = webdriver.Chrome()
            driver.get("https://portal.schule.neumuenster.de/simplesamlphp/module.php/core/loginuserpass.php?AuthState=_f4fd7ed6c4073de1d968f6c2ef8823986b102cd858%3Ahttps%3A%2F%2Fportal.schule.neumuenster.de%2Fsimplesamlphp%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fportal.schule.neumuenster.de%252Funivention%252Fsaml%252Fmetadata%26cookieTime%3D1676398292%26RelayState%3D%252Funivention%252Fportal%252F")
            sleep(3)
            search1 = driver.find_element(By.ID, "umcLoginUsername")
            search1.send_keys(myMlEmail)
            search2 = driver.find_element(By.ID, "umcLoginPassword")
            search2.send_keys(myMlPassword)
            search3 = driver.find_element(By.ID, "umcLoginSubmit")
            driver.execute_script("arguments[0].click();", search3)

        elif "öffne libreoffice" in text.lower():
            subprocess.Popen("C:\Program Files\LibreOffice\program\swriter.exe")

        for phrases in noteSTR:
            if phrases in text.lower():
                assistantResponse("Was möchtest du notieren?")
                note_text = recordAudio().lower()
                systemfunctions.note(note_text)

        if "screenshot" in text.lower():
            systemfunctions.takeScreenshot()


        if "stop" in text.lower():
            break

        assistantResponse(response)