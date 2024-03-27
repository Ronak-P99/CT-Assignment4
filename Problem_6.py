'''
Objective:
Advance your looping skills by exploring more complex list manipulations. 
You will learn to selectively loop through parts of a list, use list comprehensions for concise code, and generate numerical lists with Python's range function.

Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. 
Use slicing to create a sublist of genres from the second to the fourth track.

Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.

Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".
'''

#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
skip_first = genres[1:4]

while counter != len(skip_first):
    print(f"The track number is {counter + 1} which means the genre is {skip_first[counter]}!")
    counter += 1


#Task 2
string = ' Music'
my_new_list = [genre + string for genre in genres]
print(my_new_list)


#Task 3
num_list = [number for number in range(1,11)]
num_list.reverse()
print(f"{num_list} The beat drops now!")
