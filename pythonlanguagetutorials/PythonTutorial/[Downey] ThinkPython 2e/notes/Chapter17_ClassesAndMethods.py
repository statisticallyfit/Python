




# NOTE: compare and contrast with chapter 16 classs: there, we didn't declare attributes in class, just
# note  on the way in main function so any garbage names could be created on the fly.
# There, there were no compiler complaints that attributes weren't there.
# Here, there are complaints if you put all functions as methods and don't declare attributes.

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes time object.

        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns string representation of the time."""
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)



    def print(self):
        assert self.isValid()
        print(str(self))


    def timeToInt(self):
        """Computes number of seconds since midnight."""
        assert self.isValid()
        return self.hour * 3600 + self.minute * 60 + self.second # totalseconds


    def isAfter(self, other): # true if t1 is after t2 (later in the day than t2)
        assert self.isValid() and other.isValid()
        return self.timeToInt() > other.timeToInt()


    # note: checking the invariants (constant things that always should be true)
    def isValid(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


    def normalize(self):
        assert self.isValid()

        totalSeconds = self.timeToInt()
        return intToTime(totalSeconds)


    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds.
        """
        assert self.isValid()

        if isinstance(other, Time):
            assert other.isValid()

            seconds = self.timeToInt() + other.timeToInt()
            return intToTime(seconds)
        else:
            return self.increment(other)


    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)



    def isEqual(self, other):
        assert self.isValid() and other.isValid()

        return self.hour == other.hour and self.minute == other.minute and self.second == other.second


    def increment(self, seconds):
        assert self.isValid()

        totalSeconds = self.timeToInt() + seconds
        return intToTime(totalSeconds)



def intToTime(seconds):
    newTime = Time()
    minutesTemp, newTime.second = divmod(seconds, 60)
    newTime.hour, newTime.minute = divmod(minutesTemp, 60)
    return newTime








if __name__ == "__main__":

    t3 = Time(5, 59, 30)
    t3.print()

    t1 = Time(10, 9, 40)
    t2 = Time(10, 9, 41)
    assert not t1.isAfter(t2)
    assert t1.isAfter(t3)
    assert not t3.isAfter(t1)
    assert t2.isAfter(t1)
    assert t2.isAfter(t3)

    print("\nadd: ")
    (t1 + t2).print()
    (t1 + t3).print()
    (t3 + t2).print()
    print(Time(9, 45) + Time(1, 35))

    print("\nincrement: ")
    t1.increment(154).print()
    t2.increment(14923).print()
    t3.increment(901).print()

    assert intToTime(1495).timeToInt() == 1495
    assert t3.isEqual(intToTime(t3.timeToInt()))

    print("\n")
    start = Time(9, 45)
    end = start.increment(1337)
    start.print(); print(start) # thanks to __str__ method
    end.print()
    print("Adding const: ", start + 1337)
    print("Adding const in obj position (radd): ", 1337 + start)


    print("\nAttributes:")
    print("hour of t1: ", getattr(t1, "hour"))
    print("attributes dict: ", vars(t1))