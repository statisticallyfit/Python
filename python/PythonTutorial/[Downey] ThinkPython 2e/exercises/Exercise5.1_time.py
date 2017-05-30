import time
import math


def displayTime():
    # time in seconds since January 1 1970

    totalSeconds = time.time()
    secondsTemp = totalSeconds

    years = int(totalSeconds // (365 * 24 * 60 * 60))
    secondsTemp %= (365 * 24 * 60 * 60) # remaining secs after years taken out

    days = int(secondsTemp // (24 * 60 * 60)) # there are only days left in those secs
    secondsTemp %= (24 * 60 * 60)  # remaining secs after days taken out

    hours = int(secondsTemp // (3600)) # there are only hours left in those secs
    secondsTemp %= 3600 # remaining seconds after hours taken out

    minutes = int(secondsTemp // 60) # there are only minutes left,
    secondsTemp %= 60 # remaining seconds after minutes taken out

    seconds = int(secondsTemp) # seconds left
    #seconds += (secondsTemp % 60) # any remainder is smaller than secs ( millisecs)

    print("Back to seconds: ",
          str(years), "*(365)(24)(60)(60) + ",
          str(days), "*(24)(60)(60) + ",
          str(hours), "*(60)(60) + ",
          str(minutes), "*(60) + ",
          str(seconds), sep="")

    return (years, days, hours, minutes, seconds)
    #"{02i:%02i:%02i}".format(days, hours, minutes, seconds)



def main():
    print(displayTime())


if __name__ == '__main__':
    main()