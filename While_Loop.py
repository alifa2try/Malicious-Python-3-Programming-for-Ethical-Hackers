#!/usr/bin/env python3

# This program calculates average of student's scores using While Looping 
# Control Structure

numberOfStudents = float(input("Please enter the number of students: "))

# prints a white space
print()

totalScores = 0
studentCounter = 0

while (studentCounter < numberOfStudents):
	score = float(input("Please enter a score: "))
	totalScores = totalScores + score
	studentCounter = studentCounter + 1

#prints a white space
print()
print("The number of students entered is", studentCounter)
print("The total score for the students is", totalScores)

average = totalScores / numberOfStudents 

print("The average score is", average)
