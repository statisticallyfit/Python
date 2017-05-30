#!/usr/bin/env python3

age = int(input("Enter your age in years: "))

if(age >= 100):
	print("You've already turned 100!")
elif(age < 0):
	print("Try again after you are born!")
else:
	print("You will be 100 in " + str(100-age) + " years!")

