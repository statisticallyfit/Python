

# Getting traceback: NameError: name repeatLyrics not defined.
# repeatLyrics()


## Showing how moving the function call line generates error


def repeatLyrics():
    printLyrics()
    printLyrics()

def printLyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


repeatLyrics()