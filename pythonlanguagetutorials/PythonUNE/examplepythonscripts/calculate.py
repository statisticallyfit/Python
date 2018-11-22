#!/usr/bin/env python3

"""Perform some calculations."""

def square(x):
	"""Return the square of the given value."""
	return x * x 

def sum(a, b):
	"""Add the two given values and return the result.
	
	Keyword arguments: 
	a -- the first term to add
	b -- the second term to add
	"""
	return a + b 


print(sum(square(1), square(2)))
