# Function.py
# This program will illustrates the usage of function in python programming
# A program that uses function to find the maximum of three inputs

def maximumValue(x, y, z):
	maximum = x

	if y > maximum:
		maximum = y

	if z > maximum:
		maximum = z

	return maximum
	
# determine the maximum of three 3 integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

#invoke the maximum function
print("The maximum value of the three integers is: %d" % maximumValue(a,b,c))

# print a white space
print()

d = float(input("Enter the first floating point number: "))
e = float(input("Enter the second floating point number: "))
f = float(input("Enter the third floating point number: "))

#invoke the maximum function
print("The maximum value of the three floating point numbers is: %.2f" % maximumValue(d,e,f))

#print a white space
print()

g = input("Enter the first string: ")
h = input("Enter the second string: ")
i = input("Enter the third string: ")

#invoke the maximum function
print("The maximum value of the three integers is: %s" % maximumValue(g,h,i))
			