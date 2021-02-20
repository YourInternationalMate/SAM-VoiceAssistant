import speech_recognition as sr
import urllib.request
import re
import vlc
import pafy
import os
import pyttsx3
import datetime
import warnings
import calendar
import random
import wikipedia 
import subprocess
import requests
import webbrowser
import yaml
from time import sleep
from translate import Translator
from selenium import webdriver
import pyautogui
import face_recognition
import cv2

warnings.filterwarnings("ignore")

'''
To Do:
Autokorrektur 
Stimmenerkennung
'''


def recordAudio():      # Aufnahme und Umwandlung
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

# Funktionen

def weather(text):      # Wetter
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "in":
            return wordList[i+1]
       
def status():           # Statusbericht
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

def trans(text):        # Translator

    wordList = text.split()
    wordList.pop(0)
    lol = len(wordList)
    lang = wordList[lol-1]
    wordList.pop(lol-1)
    wordList.pop()

    if wordList[0] == "was":
        wordList.pop(0)
        if wordList[0] == "ist":
            wordList.pop(0)
            #Translaten
            print(wordList)
            transSTR = str(wordList)
            lang = umwandlungSPR(lang)
            lang = str(lang)
            translator = Translator(to_lang=(lang))
            translation = translator.translate(transSTR)
            translation = translation.strip("[&#39;")
            translation = translation.strip("&#39;]")
            return translation
    else: 
        return "Fehler"

def umwandlungSPR(lang):    # Sprachen Kürzel
    if lang == "afrikanisch":
        lang = "af"
    if lang == "irisch":
        lang = "ga"
    if lang == "albanisch":
        lang = "sq"
    if lang == "italienisch":
        lang = "it"
    if lang == "arabisch":
        lang = "ar"
    if lang == "japanisch":
        lang = "ja"
    if lang == "aserbaidschan":
        lang = "az"
    if lang == "indisch":
        lang = "kn"
    if lang == "baskisch":
        lang = "eu"
    if lang == "koreanisch":
        lang = "ko"
    if lang == "bengalisch":
        lang = "bn"
    if lang == "latein":
        lang = "la"             
    if lang == "belarusisch":
        lang = "be"
    if lang == "lettisch":
        lang = "lv"
    if lang == "bulgarisch":
        lang = "bg"
    if lang == "litauisch":
        lang = "lt"
    if lang == "katalanisch":
        lang = "ca"
    if lang == "mazedonisch":
        lang = "mk"
    if lang == "chinesisch":
        lang = "zh-CN"
    if lang == "malaiisch":     
        lang = "ms"
    if lang == "maltesisch":
        lang = "mt"
    if lang == "kroatisch":
        lang = "hr"
    if lang == "norwegisch":
        lang = "no"
    if lang == "tschechisch":
        lang = "cs" 
    if lang == "persisch":
        lang = "fa"
    if lang == "dänisch":
        lang = "da"
    if lang == "polnisch":
        lang = "pl"
    if lang == "niederländisch":
        lang = "nl"
    if lang == "portugiesisch":
        lang = "pt"
    if lang == "englisch":
        lang = "en"
    if lang == "romänisch":
        lang = "ro"
    if lang == "esperanto":
        lang = "eo"
    if lang == "russisch":
        lang = "ru"
    if lang == "estnisch":
        lang = "et"
    if lang == "serbisch":
        lang = "sr"
    if lang == "filipino":
        lang = "tk"
    if lang == "slovakisch":
        lang = "sk"
    if lang == "finnisch":
        lang = "fi"
    if lang == "slovenisch":
        lang = "sl"
    if lang == "französisch":
        lang = "fr"
    if lang == "spanisch":
        lang = "es"
    if lang == "galicisch":
        lang = "gl"
    if lang == "suaheli":
        lang = "sw"
    if lang == "georgisch": 
        lang = "ka"          
    if lang == "schwedisch":
        lang = "sv"
    if lang == "deutsch":
        lang = "de"
    if lang == "tamil":
        lang = "ta"
    if lang == "griechisch":
        lang = "el"
    if lang == "telugu":
        lang = "te"
    if lang == "gujarati":
        lang = "gu"
    if lang == "thailändisch":
        lang = "th"
    if lang == "haitianisch":
        lang = "ht"
    if lang == "türkisch":
        lang = "tr"
    if lang == "hebräisch":
        lang = "iw"
    if lang == "ukrainsich":
        lang = "uk"
    if lang == "hindi":
        lang = "hi"
    if lang == "urdu":
        lang = "ur"
    if lang == "ungarisch":
        lang = "hu"           
    if lang == "vietnamesisch":
        lang = "vi"
    if lang == "isländisch":
        lang = "is"
    if lang == "walisisch":
        lang = "cy"
    if lang == "indonesisch":
        lang = "id"
    if lang == "jiddisch":
        lang = "yi"
    return lang
  
def getDate():          # Datum
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
        weekday = "Samstag"
    if weekday == "Sunday":
        weekday = "Sonntag"
  
    return "Heute ist " + weekday + " der " + ordinalNumber[dayNum -1] + " " + month_names[monthNum -1] + "."

def getDay():           # Tag
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
        weekday = "Samstag"
    if weekday == "Sunday":
        weekday = "Sonntag"
    
    return "Heute ist " + weekday + "."

def getPerson(text):    # Leute auf Wikipedia stalken
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "wer" and wordList[i+1].lower() == "ist":
            return wordList[i+2] + " " + wordList[i+3]

def note(text):         # Notiz erstellen
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

def music(s):           # Musik abspielen
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

def login(url,usernameId, username, passwordId, password, submit_buttonId):     # Auf Moodle anmelden
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()

def takeScreenshot():   #Screenshot aufnehmen
    myScreenshot = pyautogui.screenshot()
    save_path = "unknown_faces/test"
    myScreenshot.save(save_path+".jpg")

def who_is_it():     #Gesichtserkennung
    KNOWN_FACES_DIR = 'known_faces'
    UNKNOWN_FACES_DIR = 'unknown_faces'
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = 'cnn'  



    def name_to_color(name):
        
        color = [(ord(c.lower())-97)*8 for c in name[:3]]
        return color


    print('Loading known faces...')
    assistantResponse("Lade bekannte Gesichter.")
    known_faces = []
    known_names = []


    for name in os.listdir(KNOWN_FACES_DIR):

        
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

            
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

        
            encoding = face_recognition.face_encodings(image)[0]

            
            known_faces.append(encoding)
            known_names.append(name)


    print('Processing unknown faces...')
    assistantResponse("Lade Unbekannte Gesichter.")

    for filename in os.listdir(UNKNOWN_FACES_DIR):

        
        print(f'Filename {filename}', end='')
        image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

        
        locations = face_recognition.face_locations(image, model=MODEL)

        
        encodings = face_recognition.face_encodings(image, locations)

        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        
        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):

            
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

            
            match = None
            if True in results:  
                match = known_names[results.index(True)]
                print(f' - {match} from {results}')
                assistantResponse(match)

            
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                
                color = name_to_color(match)

                
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

    
        cv2.imshow(filename, image)
        


# MAIN

weatherSTR = ["grad", "wetter"]
time_str = ["wie viel uhr", "wie spät"]
date_str = ["der wievielte", "den wievielten"]

assistantResponse("Hallo ich bin Sam.")

while True:
    text = recordAudio()
    response = ""
    if wakeWord(text) == True:


        if "was ist" in text.lower():
            tran = trans(text)
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
                get_date = getDate() 
                response = response + "" + get_date   

        if "welcher tag" and "heute" in text.lower():
            response = response + getDay()
            
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

        elif "wer ist das" in text.lower():
            takeScreenshot()
            who_is_it()
            os.remove("unknown_faces/test.jpg")

        elif "wer ist" in text.lower():
            assistantResponse("Ich suche auf Wikipedia")
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            lang = "de"
            translator = Translator(to_lang=(lang))
            wiki = translator.translate(wiki)
            assistantResponse("Laut Wikipedia")
            response = response + " " + wiki

        elif "song" in text.lower():
            assistantResponse("Was willst du suchen?")
            search = recordAudio()           
            music(search)
            
        elif "öffne google" in text.lower():
            webbrowser.open("chrome")

        elif "öffne youtube" in text.lower():
            chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chromedir).open("http://youtube.com/")
            
        elif "öffne moodle" in text.lower():
            conf = yaml.load(open('loginDetails.yml'))
            myMlEmail = conf['ml_user']['email']
            myMlPassword = conf['ml_user']['password']
            driver = webdriver.Chrome()
            login("https://portal.schule.neumuenster.de/simplesamlphp/module.php/core/loginuserpass.php?AuthState=_110d1ecc49e53565db44217b463b575b5ea2681e7b%3Ahttps%3A%2F%2Fportal.schule.neumuenster.de%2Fsimplesamlphp%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fportal.schule.neumuenster.de%252Funivention%252Fsaml%252Fmetadata%26cookieTime%3D1613733618%26RelayState%3D%252Funivention%252Fportal%252F", "umcLoginUsername", myMlEmail, "umcLoginPassword", myMlPassword, "umcLoginSubmit")

        noteSTR = ["erstelle eine notiz", "erstelle eine datei", "make a note", "erstell eine notiz", "notiz erstellen"]
        for phrases in noteSTR:
            if phrases in text.lower():
                assistantResponse("Was möchtest du notieren?")
                note_text = recordAudio().lower()
                note(note_text)
        if "screenshot" in text.lower():
            takeScreenshot()


        if "stop" in text.lower():
            break

        assistantResponse(response)
