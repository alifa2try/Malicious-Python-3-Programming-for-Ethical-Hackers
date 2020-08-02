#!/usr/bin/env python3

# This program performs basic arithmetic operations

# Enter the first number
firstNumber = float(input("Enter the first number: "))

# Enter the second number
secondNumber = float(input("Enter the second number: "))

print()

# Addition operation
addition = firstNumber + secondNumber 

# Subtraction operation
difference = firstNumber - secondNumber

# Multiplication operation
product = firstNumber * secondNumber

# Division operation
division = firstNumber / secondNumber

# Modulo operation
modulo = firstNumber % secondNumber
		
# print the summation result
print("The summation of the two numbers is: %.2f" % addition)

# print the difference result
print("The difference between the two numbers is: %.2f" % difference)

# print the product result
print("The product of the two numbers is: %.2f" % product)

# print out the division result
print("The division of the two numbers is: %.2f" % division)

# print the modulo result
print("The modulo operation of the two numbers is: %.2f" % modulo)
