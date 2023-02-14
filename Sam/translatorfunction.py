from translate import Translator

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