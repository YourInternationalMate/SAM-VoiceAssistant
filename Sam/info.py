import datetime
import calendar
import requests

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