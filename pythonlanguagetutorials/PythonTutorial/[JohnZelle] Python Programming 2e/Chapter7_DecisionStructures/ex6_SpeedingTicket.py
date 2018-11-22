

def calculateFine(speedLimit, clockedSpeed):
    fine = 0.0

    if clockedSpeed > speedLimit:
        fine += 50 + 5*(clockedSpeed - speedLimit)

    if clockedSpeed > 90:
        fine += 200

    # Now evaluate:
    if fine == 0.0:
        print("The speed was legal.")
    else:
        print("The speed was illegal. Fine = ${0:.2f}".format(fine))




if __name__ == "__main__":
    calculateFine(60, 56)
    calculateFine(60, 70.458)
    calculateFine(60, 120.34111)