#!/usr/bin/env python3

# This program introduces the comparison operators and if selection statement

print("Hello friend enter two integers and I am going to tell you the relationship they satisfy")
firstNumber = (int(input("Enter the first number: ")))
secondNumber = (int(input("Enter the second number: ")))

if (firstNumber > secondNumber):
	print(firstNumber, "is greater than", secondNumber)

if (firstNumber < secondNumber):
	print(firstNumber, "is less than", secondNumber)

if (firstNumber >= secondNumber):
	print(firstNumber, "is greater than or equal to", secondNumber)

if (firstNumber <= secondNumber):
	print(firstNumber, "is less than or equal to", secondNumber)

if (firstNumber == secondNumber):
	print(firstNumber, "is equal to", secondNumber)




