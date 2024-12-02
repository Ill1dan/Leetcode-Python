def isPrefixOfWord(sentence, searchWord):
    window = len(searchWord)

    for res, word in enumerate(sentence.split()):
        if word[:window] == searchWord:
            return res + 1

    return -1


sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence, searchWord))