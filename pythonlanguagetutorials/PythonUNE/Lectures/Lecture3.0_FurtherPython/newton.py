#!/usr/bin/env python3

epsilon = 0.0000000000000000000000000000000000000000000000000001

square = input("Enter a value to find the root of: ")
a = float(square)
estimate = input("Enter initial estimate of root: ")
x = float(estimate)

while True:
	print(x)
	y = (x + a/x)/2
	if(abs(x - y) < epsilon):
		break
	# otherwise set x = y
	x = y # to get new updated estimate

print(x)
