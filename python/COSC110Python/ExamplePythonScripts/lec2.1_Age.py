#!/usr/bin/env python3

""" Return the user's age in years """
ageInput = input("Enter your age in years: ")
ageInYears = int(ageInput)
ageInDays = ageInYears * 365
print("You are approximately", ageInDays, "days old")
