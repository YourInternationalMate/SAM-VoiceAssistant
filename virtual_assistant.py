'''
Musik abspielen
Wetter (Temperatur)
Translater
Autokorrektur 
Bilder erkennen (was drauf ist)
Nachrichten schreiben lassen
Statusbericht (Wetter, Zeit, Datum)
'''





import speech_recognition as sr
import os
import pyttsx3
import datetime
import warnings
import calendar
import random
import wikipedia 
import subprocess


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
    WAKE_WORDS = ["jarvis", "travis", "travers", "davis"]

    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
        
    return False

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

def getProgramm(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "starte" or wordList[i].lower() == "öffne":
            return wordList[i+1] 

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

#main

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


        if "wer ist" in text.lower():
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + " " + wiki


        noteSTR = ["erstelle eine notiz", "make a note", "erstell eine notiz", "notiz erstellen"]
        for phrases in noteSTR:
            if phrases in text.lower():
                assistantResponse("Was möchtest du notieren?")
                note_text = recordAudio().lower()
                note(note_text)

        
        
        if "stop" in text.lower():
            break

        assistantResponse(response)



