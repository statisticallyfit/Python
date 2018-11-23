

def countNumWords(sentence):
    """Counts number of words in the sentence string."""
    wordCount = 0

    words = sentence.split() # split at whitespace
    for word in words:
        wordHasSomeLetters = any(letter.isalpha() for letter in list(word))
        if wordHasSomeLetters:
             wordCount += 1
    return wordCount


if __name__ == "__main__":
    assert countNumWords("Hi there . the pumpkin in the rain") == 7
    assert countNumWords("The sky turns orange, in the thunderstorm.") == 7
    assert countNumWords("Hi there . the pumpkin in the ;;;0rain *&") == 7

