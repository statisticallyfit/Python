
import sys
sys.path.append('../')
from notes.Chapter16_ClassesAndFunctions import Time, printTime, isAfter, addTime, isEqualTime, normalize, intToTime, timeToInt, increment, isValidTime
# note: very important above code: how to import from other directory.




def mulTime(time, number):
    assert isValidTime(time)
    return intToTime(timeToInt(time) * number)


def averagePace(raceFinishTime, distance):
    return mulTime(raceFinishTime, 1 / distance) # the average pace (time per mile)

if __name__ == "__main__":
    t = Time()
    t.hour, t.minute, t.second = 4, 10, 15

    printTime(averagePace(t, 16))

