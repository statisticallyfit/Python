


def getSentenceInput():
    sentence = input("Enter a sentence: ")
    return sentence

def getPureWords(sentence):
    """Gets a list of words in which at least some chars are letters
    (not all punctuation or digits)."""
    pureWords = []
    words = sentence.split() # split at whitespace
    for word in words:
        wordHasSomeLetters = any(letter.isalpha() for letter in list(word))
        if wordHasSomeLetters:
             pureWords.append(word)
    return pureWords


def countAverageWordLength(sentence):
    #sentence = getSentenceInput()
    words = getPureWords(sentence)
    wordLenSum = 0

    for word in words:
        wordLenSum += len(word)

    return wordLenSum * 1.0 / len(words)


def countAverageWordLength_UserInput():
    sentence = getSentenceInput()
    words = getPureWords(sentence)
    wordLenSum = 0

    for word in words:
        wordLenSum += len(word)

    return wordLenSum * 1.0 / len(words)



if __name__ == "__main__":
    print(countAverageWordLength("Hi there . the pumpkin in the rain"))
    print(countAverageWordLength("The sky turns orange, in the thunderstorm."))
    print(countAverageWordLength("Hi there . the pumpkin in the ;;;0rain *&"))

    print(countAverageWordLength_UserInput())