#!/usr/bin/env python3

# A program to calculate the sum of even numbers from 2 to 100 using For loop

# A variable to hold the sum of the even numbers
sum = 0

for number in range(2, 101, 2):
	sum += number

print("The summation of even numbers from 2 to 100 is %d" % sum)	

