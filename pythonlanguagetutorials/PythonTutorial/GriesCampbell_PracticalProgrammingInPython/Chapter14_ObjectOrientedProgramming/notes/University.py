

class Member:
    """Member of university."""

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return "Name: {0}\nAddress: {1}\nEmail: {2}".format(self.name, self.address, self.email)


class Faculty(Member):

    def __init__(self, name, address, email, facultyID, courses):
        super().__init__(name, address, email)
        self.facultyID = facultyID
        self.coursesTeaching = courses

    def __str__(self):
        memberStr = super().__str__()

        return "{}\nFaculty ID: {}\nCourses Teaching: {}".format(memberStr, self.facultyID, ", ".join(self.coursesTeaching))


class Student(Member):

    def __init__(self, name, address, email, studentID, taken, taking):
        super().__init__(name, address, email)
        self.studentID = studentID
        self.coursesTaken = taken
        self.coursesTaking = taking

    def __str__(self):
        memberStr = super().__str__()
        return "{}\nStudent ID: {}\nCourses Taken: {}\nCourses Taking: {}"\
            .format(memberStr, self.studentID,
                    ", ".join(self.coursesTaken),", ".join(self.coursesTaking))



if __name__ == "__main__":
    jenna = Faculty("Jenna Banda", "Egypt", "jbanda@princess.roy", "8315", ["Knitting", "Sword-fighting"])
    beetle = Student("Bobby Beetle", "Egypt", "bbeetle@workshop.srv", "1043", ["Communication"], ["Writing", "Stamping"])
    septimus = Student("Septimus Heap", "Egypt", "sheap@apprentice.srv", "4058", ["Army"], ["Magic", "Physik"])
    snorri = Student("Snorri Snorrelson", "Arctic", "ssnore@trader.exp", "7198", ["Whale-caring"], ["Ship-building", "Captaining"])

    lst = [jenna, beetle, septimus, snorri]
    for item in lst:
        print(item)
        print("")
