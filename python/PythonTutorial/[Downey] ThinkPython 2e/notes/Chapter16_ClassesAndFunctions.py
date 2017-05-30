
class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def printTime(time):
    assert isValidTime(time)

    # note: use this instead of below because the below won't round if decimals.
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    # print("{0:02d}:{1:02d}:{2:02d}".format(time.hour, time.minute, time.second))


def isAfter(t1, t2): # true if t1 is after t2 (later in the day than t2)
    assert isValidTime(t1) and isValidTime(t2)

    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)



def normalizeSlow(time):
    import copy
    timeCopy = copy.deepcopy(time)

    while timeCopy.second >= 60:
        timeCopy.second -= 60
        timeCopy.minute += 1

    while timeCopy.minute >= 60:
        timeCopy.minute -= 60
        timeCopy.hour += 1
    return timeCopy




def normalize(time):
    assert isValidTime(time)

    totalSeconds = timeToInt(time)
    return intToTime(totalSeconds)


def intToTime(seconds):
    newTime = Time()
    minutes, newTime.second = divmod(seconds, 60)
    newTime.hour, newTime.minute = divmod(minutes, 60)
    return newTime


def timeToInt(time):
    assert isValidTime(time)

    return time.hour * 3600 + time.minute * 60 + time.second



# note: pure function: modifies none of the arg functions, and has no effect (no IO or input)
def addTime(t1, t2):
    assert isValidTime(t1) and isValidTime(t2)

    seconds = timeToInt(t1) + timeToInt(t2)
    return intToTime(seconds)


def isEqualTime(t1, t2):
    assert isValidTime(t1) and isValidTime(t2)

    return t1.hour == t2.hour and t1.minute == t2.minute and t1.second == t2.second


# note: modifier function: changes objects it gets as parameters: changes are visible to the caller.
def increment(time, seconds):
    assert isValidTime(time)

    totalSeconds = timeToInt(time) + seconds
    return intToTime(totalSeconds)



# note: checking the invariants (constant things that always should be true)
def isValidTime(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


if __name__ == "__main__":

    t3 = Time()
    t3.hour = 5
    t3.minute = 59
    t3.second = 30
    printTime(t3)

    t1 = Time(); t1.hour, t1.minute, t1.second = 10, 9, 40
    t2 = Time(); t2.hour, t2.minute, t2.second = 10, 9, 41
    assert not isAfter(t1, t2)
    assert isAfter(t1, t3)
    assert not isAfter(t3, t1)
    assert isAfter(t2, t1)
    assert isAfter(t2, t3)

    print("\nadd: ")
    printTime(addTime(t1, t2))
    printTime(addTime(t1, t3))
    printTime(addTime(t3, t2))

    print("\nincrement: ")
    printTime(increment(t1, 154))
    printTime(increment(t2, 14923))
    printTime(increment(t3, 901))


    assert timeToInt(intToTime(1495)) == 1495
    assert isEqualTime(intToTime(timeToInt(t3)), t3)