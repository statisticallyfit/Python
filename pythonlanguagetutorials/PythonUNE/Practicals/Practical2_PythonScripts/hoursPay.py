#!/usr/bin/env python3

hours = int(input("How many hours did you work?" ))
# use cents because floats are not exact so use ints
payPerHour = 100 * int(input("How much do you get paid per hour?" ))

payCents = payPerHour * hours

if(hours < 10):
	payCents += payPerHour * 1
elif(hours > 10):
	payCents += payPerHour * 5

payDollars = round(payCents/100, 2)
print("Pay due: $", payDollars)
