import sys
sys.path.append('../')
from notes.Chapter16_ClassesAndFunctions import Time, printTime, isAfter, addTime, isEqualTime, normalize, intToTime, timeToInt, increment, isValidTime

from datetime import * # we import datetime.datetime as well here.
import calendar

# part 1
def getCurrentDateAndWeekday():
    now = date.today()
    weekdayList= calendar.day_name

    return (now.year, now.month, now.day, weekdayList[now.weekday()])


def ageAndNumDaysToNextBirthday(birthday):
    #def cleanConvert(st): return int(st.strip("0").strip())

    #year, month, day = input("Input yy/mm/dd of birthday: ").split("/")
    #year, month, day = cleanConvert(year), cleanConvert(month), cleanConvert(day)

    #birthday = datetime(year, month, day)
    today = datetime.today()

    # note: you are: years,  days... and hours, mins, seconds years old (skipping months)
    ageDelta = today - birthday

    # note: getting the number of days, hours, minutes, seconds until next birthday
    nextBirthday = datetime(today.year, birthday.month, birthday.day)
    if nextBirthday < today: # if birthday already passed, then we have next year
        nextBirthday = datetime(today.year + 1, birthday.month, birthday.day)

    nextBirthdayDelta = nextBirthday - today
    return (describeDelta(ageDelta), describeDelta(nextBirthdayDelta))


def describeDelta(deltaObj):
    mins, secs = divmod(deltaObj.seconds + deltaObj.days * 86400, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    return (years, days, hours, mins, secs)

def printDelta(delta):
    print("years={0}, days={1}, {2:02d}:{3:02d}:{4:02d}".format(delta[0], delta[1], delta[2], delta[3], delta[4]))



# 3 - double day is when one bday is twice as old as the other
def computeDoubleDay(bday1, bday2):
    # note: bday2 = farther in calendar - younger person
    # note: bday1 = before in calendar - older person
    assert bday2 > bday1
    delta = bday2 - bday1
    doubleDay = bday2 + delta
    return doubleDay


if __name__ == "__main__":
    # 1
    print(getCurrentDateAndWeekday())
    print(date.today().strftime("%A")) # or could have used this

    # 2
    age, nextB = ageAndNumDaysToNextBirthday(datetime(1997, 4, 23))
    print("\n")
    printDelta(age)
    printDelta(nextB)

    # 3
    bday1 = datetime(2006, 12, 26)
    bday2 = datetime(2003, 10, 11)
    print("\nDouble day:")
    assert bday1 > bday2
    print(computeDoubleDay(bday2, bday1))
