

def grade(score):
    if score >= 90 and score <= 100:
        return "A"
    if score >= 80 and score <= 89:
        return "B"
    if score >= 70 and score <= 79:
        return "C"
    if score >= 60 and score <= 69:
        return "D"
    else:
        return "F"


print(grade(100))
print(grade(10))
print(grade(90))
print(grade(75))
print(grade(85))
