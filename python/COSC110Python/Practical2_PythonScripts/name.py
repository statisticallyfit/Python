#!/usr/bin/env python3

name = input("Please enter your  name: ")
print("Hello " + name + "!\n")

first = input("first number: ")
first = int(first)

second = int(input("second number: " ))

if first < second:
	print(first, " < ", second)
elif second < first:
	print(first, " > ", second)
else:
	print(first, " == ", second)
	print("did you do that on purpose?")

average = (first + second)/2
print("Average: " + str(average))
