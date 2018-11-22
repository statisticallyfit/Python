#!/usr/bin/env python3

# another infinite loop look-alike

n = 0
while True:
	line = input("Exit? ")
	if(line == "y" or line == "Y"):
		break
	print("We'll loop again")
	n += 1
print("Done: ", n)
