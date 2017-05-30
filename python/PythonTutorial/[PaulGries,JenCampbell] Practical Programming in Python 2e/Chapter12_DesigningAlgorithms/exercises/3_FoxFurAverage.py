


def averageNumPelts(fileName):
    # reading in data
    peltNumsYearly = []

    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        if line.isdigit():# checks if all chars in string are digits!
            peltNumsYearly.append(int(line))
    fileIn.close()

    # finding average
    return sum(peltNumsYearly) * 1.0 / len(peltNumsYearly)



if __name__ == "__main__":
    print(averageNumPelts("hopedale.txt"))
