'''
Musik abspielen - :check:
Translater -
Autokorrektur 
Bilder erkennen (was drauf ist)
'''


import speech_recognition as sr
import urllib.request
import re
import vlc
import pafy
from time import sleep
import os
import pyttsx3
import datetime
import warnings
import calendar
import random
import wikipedia 
import subprocess
import requests


warnings.filterwarnings("ignore")

# Aufnahme und Umwandlung
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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

def assistantResponse(text):
    print(text)
    engine = pyttsx3.init()
    engine. setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    

def wakeWord(text):
    WAKE_WORDS = ["sam"]

    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
        
    return False
def weather(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "in":
            return wordList[i+1]
       
def status():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    
    month_names = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    ordinalNumber = ["Erste", "Zweite", " Dritte", "Vierte", " Fünfte", "Sechste", "Siebte", "Achte", "Neunte", "Zehnte", "Elfte", "Zwölfte", "Dreizehnte", "Vierzehnte", "Fünfzehnte",
    "Sechzehnte", "Siebzehnte", "Achtzehnte", "Neunzehnte", "Zwanzigste", "Einundzwanzigste", "Zweiundzwanzigste", "Dreiundzwanzigste", "Vierundzwanzigste", "Fünfundzwanzigste", "Sechsundzwanzigste",
    "Siebenundzwanzigste", "Achtundzwanzigste", "Neunundzwanzigste", "Dreißigste","Einunddreißigste"]

    if weekday == "Monday":
        weekday = "Montag"
    if weekday == "Tuesday":
        weekday = "Dienstag"
    if weekday == "Wednesday":
        weekday = "Mittwoch"
    if weekday == "Thursday":
        weekday = "Donnerstag"
    if weekday == "Friday":
        weekday = "Freitag"
    if weekday == "Saturday":
        weekday = "Samsatg"
    if weekday == "Sunday":
        weekday = "Sonntag"

    
   
    user_api = "989fd048fb579d6222799cb5d1e294d9"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=Neumünster&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city = ((api_data['main']['temp']) - 273.15)
    temp_city = int(temp_city)
    temp_city = str(temp_city)
  
    return "Heute ist " + weekday + " der " + ordinalNumber[dayNum -1] + " " + month_names[monthNum -1] + ". In Neumünster sind aktuell " + temp_city + " Grad."

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    ordinalNumber = ["Erste", "Zweite", " Dritte", "Vierte", " Fünfte", "Sechste", "Siebte", "Achte", "Neunte", "Zehnte", "Elfte", "Zwölfte", "Dreizehnte", "Vierzehnte", "Fünfzehnte",
    "Sechzehnte", "Siebzehnte", "Achtzehnte", "Neunzehnte", "Zwanzigste", "Einundzwanzigste", "Zweiundzwanzigste", "Dreiundzwanzigste", "Vierundzwanzigste", "Fünfundzwanzigste", "Sechsundzwanzigste",
    "Siebenundzwanzigste", "Achtundzwanzigste", "Neunundzwanzigste", "Dreißigste","Einunddreißigste"]

    if weekday == "Monday":
        weekday = "Montag"
    if weekday == "Tuesday":
        weekday = "Dienstag"
    if weekday == "Wednesday":
        weekday = "Mittwoch"
    if weekday == "Thursday":
        weekday = "Donnerstag"
    if weekday == "Friday":
        weekday = "Freitag"
    if weekday == "Saturday":
        weekday = "Samsatg"
    if weekday == "Sunday":
        weekday = "Sonntag"
  
    return "Heute ist " + weekday + " der " + ordinalNumber[dayNum -1] + " " + month_names[monthNum -1] + "."

def getDay():
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    if weekday == "Monday":
        weekday = "Montag"
    if weekday == "Tuesday":
        weekday = "Dienstag"
    if weekday == "Wednesday":
        weekday = "Mittwoch"
    if weekday == "Thursday":
        weekday = "Donnerstag"
    if weekday == "Friday":
        weekday = "Freitag"
    if weekday == "Saturday":
        weekday = "Samsatg"
    if weekday == "Sunday":
        weekday = "Sonntag"
    
    return "Heute ist " + weekday + "."

def greeting(text):
    GREETING_INPUTS = ["hi", "hey", "moin", "na", "hallo", "hello", "hola"]
    GREETING_RESPONSES = ["wie gehts", "na", "guten tag", "hola", "schön dich zu sehen", "howdy"]

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + ". "
    return ""

def getPerson(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "wer" and wordList[i+1].lower() == "ist":
            return wordList[i+2] + " " + wordList[i+3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

def music(s):
    s = str(s)
    s = s.replace(" ", "%")
    yturl = "https://www.youtube.com/results?search_query="
    ytsearch = str(yturl) + str(s)
    html = urllib.request.urlopen(ytsearch)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://youtu.be/" + video_ids[0]
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    ins = vlc.Instance()
    player = ins.media_player_new()

    code = urllib.request.urlopen(url).getcode()
    if str(code).startswith('2') or str(code).startswith('3'):
        print('Stream is working')
    else:
        print('Stream is dead')

    Media = ins.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    vol = 50
    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    duration = player.get_length()
    print("Das Lied geht:",duration,"Minuten")
    while str(player.get_state()) in good_states:
        player.audio_set_volume(vol) 
        c = recordAudio()
        if "stopp" in c.lower():
            player.stop()
            print(c)
        elif "leiser" in c.lower():
            vol -= 10 
        elif "lauter" in c.lower():
            vol += 10
        else:
            c = ""
        
    player.stop()




#main

assistantResponse("Hallo, ich bin Sam dein virtueller Assistent, wie kann ich dir helfen?")

while True:
    text = recordAudio()
    response = ""
    if wakeWord(text) == True:
        response = response + greeting(text)

        time_str = ["wie viel uhr", "wie spät"]
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

        date_str = ["der wievielte", "den wievielten"]
        for phrases in date_str:
            if phrases in text.lower():
                get_date = getDate() 
                response = response + "" + get_date   

        if "welcher tag" and "heute" in text.lower():
            response = response + getDay()
            
        weatherSTR = ["grad", "wetter"]
        for phrases in weatherSTR:
            if phrases in text.lower():
                wetter = weather(text)
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
            statusV = status()
            response = response + statusV

        if "wer ist" in text.lower():
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + " " + wiki

        if "song" in text.lower():
            assistantResponse("Was willst du suchen?")
            search = recordAudio()           
            music(search)

        noteSTR = ["erstelle eine notiz", "erstelle eine datei", "make a note", "erstell eine notiz", "notiz erstellen"]
        for phrases in noteSTR:
            if phrases in text.lower():
                assistantResponse("Was möchtest du notieren?")
                note_text = recordAudio().lower()
                note(note_text)


        
        if "stop" in text.lower():
            break

        assistantResponse(response)




