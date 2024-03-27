'''
Objective:
The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
'''

import random 

item_list = ["Table", "Spoon", "Fork", "Dish"]
user_guess = "nothing"
my_guess = random.choice(item_list)

while user_guess != my_guess:
  user_guess = input("Welcome! Please choose between a Table, Spoon, Fork, or Dish (Case Sensitive): ")

  if user_guess != my_guess:
    print(f"Oops! {user_guess} doesn't match my guess! Try again.")
  else:
        print(f"Congrats! We both guessed: {my_guess}!")


