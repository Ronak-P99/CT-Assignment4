'''
Objective:
The aim of this assignment is to practice using nested loops in Python. 
You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
For each time, randomly select a mood from a predefined list and print it.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"
'''
#I used my code from previous problem and added onto it
import random 

mood = ["Happy", "Sad", "Energetic", "Calm"]
days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

for day in range(0, len(days_week)):
    for time in time_of_day:
        print(f"On {days_week[day]} {time}, " + "you were feeling " + random.choice(mood) + ".")