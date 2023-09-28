import speech_recognition as sr
import pyttsx3
import warnings
import requests
import webbrowser

# Importieren Sie Ihre eigenen Module hier
import info
import systemfunctions
import translatorfunction
import weather
import wiki
import google

warnings.filterwarnings("ignore")

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty("rate", 170)
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)

    def record_audio(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
        try:
            data = self.recognizer.recognize_google(audio, language="de")
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Das habe ich leider nicht verstanden")
            return ""
        except sr.RequestError as e:
            print("Service-Fehler: " + str(e))
            return ""

    def assistant_response(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def google_search(self, query):
        # Führen Sie die Google-Suchfunktion aus
        response = "Hier ist das Ergebnis."
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return response

    def run(self):
        self.assistant_response("Hallo ich bin Sam.")

        while True:
            text = self.record_audio()
            response = ""

            if "google" in text:
                query = text.replace("google", "").strip()
                response = self.google_search(query)

            if "was ist" in text:
                translation = translatorfunction.trans(text)
                response = translation

            if "wie viel uhr" in text or "wie spät" in text:
                time = info.get_time()
                response = f"Es ist {time} Uhr."

            if "der wievielte" in text or "den wievielten" in text:
                date = info.get_date()
                response = f"Heute ist der {date}."

            if "welcher tag heute" in text:
                day = info.get_day()
                response = f"Heute ist {day}."

            if "grad" in text or "wetter" in text:
                weather_info = weather.weather(text)
                response = f"Die Temperatur beträgt {weather_info} Grad Celsius."

            if "status" in text:
                status_info = info.status()
                response = f"Der Status ist: {status_info}."

            if "wer ist das" in text:
                systemfunctions.take_screenshot()
                recognizer.who_is_it()
                sleep(10)
                systemfunctions.remove_screenshot()
                response = "Die Identifikation ist fertig."

            if "wer ist" in text:
                self.assistant_response("Ich suche auf Wikipedia.")
                person = wiki.get_person(text)
                wiki_summary = wiki.get_summary(person)
                translation = translatorfunction.trans(wiki_summary)
                self.assistant_response(f"Laut Wikipedia: {translation}")
                response = f"Laut Wikipedia: {translation}"

            if "öffne google" in text:
                webbrowser.open("https://www.google.com")
                response = "Google wurde geöffnet."

            if "öffne youtube" in text:
                webbrowser.open("https://www.youtube.com")
                response = "Youtube wurde geöffnet."

            if "öffne libreoffice" in text:
                systemfunctions.open_libreoffice()
                response = "LibreOffice wurde gestartet."

            if "erstelle eine notiz" in text:
                self.assistant_response("Was möchtest du notieren?")
                note_text = self.record_audio().lower()
                systemfunctions.create_note(note_text)
                response = "Notiz wurde erstellt."

            if "wer bist du" in text or "was bist du" in text:
                response = "Ich bin Sam, ein virtueller Assistent."

            if "screenshot" in text:
                systemfunctions.take_screenshot()
                response = "Ein Screenshot wurde erstellt."

            if "stop" in text:
                exit()

            self.assistant_response(response)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()
