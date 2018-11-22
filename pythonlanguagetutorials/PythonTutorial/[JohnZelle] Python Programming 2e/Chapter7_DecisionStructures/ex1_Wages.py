
def getJobInput():

    numHours = input("Enter number of hours worked this week: ")
    while True:
        try:
            numHours = int(numHours)
        except ValueError:
            print("Invalid. Enter number of hours worked: ")
        else:
            break


    hourlyRate = input("Enter the hourly rate for this week: ")
    while True:
        try:
            hourlyRate = float(hourlyRate)
        except ValueError:
            print("Invalid. Enter hourly rate: ")
        else:
            break
    return (numHours, hourlyRate)


def calculateWeeklyWages():
    numHours, hourlyRate = getJobInput()
    totalWages = 0
    if numHours > 40:
        totalWages += (numHours - 40) * (hourlyRate + 0.5)
        totalWages += 40 * hourlyRate # the actual 40 hours before the above ones
    else:
        totalWages += numHours * hourlyRate

    return totalWages


if __name__ == "__main__":
    print(calculateWeeklyWages())