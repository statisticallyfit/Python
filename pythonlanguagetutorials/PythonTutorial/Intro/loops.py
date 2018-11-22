""" while loop

x = 10
while x != 0:
    print(x)
    x = x - 1
    print("Decrementing x... Now equals: ", str(x))
print("End loop")

"""
#______________________________________________________

""" TO FIX: Bugs!!!


print("\n\n\n\nGetting input to do conditional statement")
#input([Prompt])
num = input("Please enter a number from 1 to 10, inclusive\n")
if num == 5:
    print("Hooray! You guessed correct")
else:
    print("Sorry you didn't enter the right number")

"""
#______________________________________________________
"""
print("\n\n\nPrinting even numbers up to 20...")

n = 0
while n <= 20:
    if n % 2 == 0:
        print(n)
    n = n + 1
print("Done")

"""
#______________________________________________________

"""
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3,6):
    print(x)

"""

# Prints out 0,1,2,3,4
"""
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("\n\n")

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    """
#______________________________________________________

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

print("The even numbers:")
for x in numbers:
    # print only ALL EVEN numbers in list, just no 237
    if x == 237:
        print("We have reached the magic 237! Break here")
        break
    if x % 2 == 0:      # check for even numbers
        print(x)



