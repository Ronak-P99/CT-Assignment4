'''
Objective:
The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. 
You will correct a code snippet, simulate moods for different days, and create a countdown timer.

Task 1: Your Mood Today
Write a program that prints off different moods for each day of the week. 
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. 
Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
'''
import random 

mood = ["Happy", "Sad", "Energetic", "Calm"]
days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(0, len(days_week)):
    print(f"Today is {days_week[day]}, " + "you were feeling " + random.choice(mood) + ".")