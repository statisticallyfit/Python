
import random




def totalWeight(available, weight):
    total = 0

    for key in weight:
        total += weight.get(key) * available.get(key)

    return total



weight = {"pencil": 10, "pen": 20, "paper": 4, "eraser": 80}
available = {"pencil": 5, "pen": 3, "paper": 10, "eraser": 2}


print(totalWeight(available, weight))



# ----------------------
# part 4 not to submit
for i in range(10):
    randVal = random.random()
    print(randVal)

print("choice: ", random.choice(range(20)))


# select between 1 and 20
def guessing():
    target = random.randint(1, 20)
    guess = 0

    while guess != target:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")

    print("You got it!: ", guess, target)

guessing()
