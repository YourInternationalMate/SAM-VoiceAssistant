def getPerson(text):    # Leute auf Wikipedia stalken
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i +3 <= len(wordList) - 1 and wordList[i].lower() == "wer" and wordList[i+1].lower() == "ist":
            return wordList[i+2] + " " + wordList[i+3]