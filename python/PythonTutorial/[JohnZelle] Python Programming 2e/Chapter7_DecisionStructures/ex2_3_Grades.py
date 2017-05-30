

pointGrades = {5: "A", 4: "B", 3: "C", 2: "D", 1: "F", 0:"F"}


def scoreToGrade(quizScore):
    return pointGrades.get(quizScore)


def scoreToGradeExam(examScore):
    if 90 <= examScore <= 100:
        return "A"
    if 80 <= examScore <= 89:
        return "B"
    if 70 <= examScore <= 79:
        return "C"
    if 60 <= examScore <= 69:
        return "D"
    if examScore < 60:
        return "F"



if __name__ == "__main__":
    assert scoreToGrade(5) == "A"
    assert scoreToGrade(4) == "B"
    assert scoreToGrade(3) == "C"
    assert scoreToGrade(2) == "D"
    assert scoreToGrade(1) == "F"
    assert scoreToGrade(0) == "F"


    assert scoreToGradeExam(100) == "A"
    assert scoreToGradeExam(101) == None
    assert scoreToGradeExam(95) == "A"
    assert scoreToGradeExam(90) == "A"
    assert scoreToGradeExam(100) == "A"
    assert scoreToGradeExam(100) == "A"
    assert scoreToGradeExam(100) == "A"
    assert scoreToGradeExam(100) == "A"
    assert scoreToGradeExam(100) == "A"