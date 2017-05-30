#!/usr/bin/env python3

# assume entering a positive number else infinite loop.
start = int(input("Enter a number: "))
n = start 

# not always easy to tell whether loop will exit. 
# Collatz conjecture - no number found yet that makes infinite loop.
while n != 1:
	print(n)
	if(n % 2 == 0):
		n = n // 2 # floor division => int not floating point
	else: #n is odd
		n = 3 * n + 1 # result is even (because 3*odd +1 is even)
print("Complete")
