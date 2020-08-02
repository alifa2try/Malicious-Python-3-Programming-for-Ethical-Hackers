#!/usr/bin/env python3

# This program uses multiple if selection structure to create a program that
# will decide a students grade based on the following criteria:
# A: 70 - 100; B: 60 - 69; C: 50 -59; D: 45 - 49; E: 40 - 44; F: 0 - 39;

score = float(input("Enter the score: "))

if (score > 100):
	print("Invalid entry. Please enter a score between 0 - 100")
	raise SystemExit
elif (score < 0):
	print("Invalid entry. Please enter a score between 0 - 100")
	raise SystemExit
elif (score >= 70):
	print("The student grade is A")
elif (score >= 60):
	print("The student grade is B")
elif (score >= 50):
	print("The student grade is C")	
elif (score >= 45):
	print("The student grade is D")	
elif (score >= 40):
	print("The student grade is E")
else:
	print("The student grade is F")	
