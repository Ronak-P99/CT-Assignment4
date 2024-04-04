'''
Objective:
Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose.
By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. 
Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. 
Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.
'''

#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 1
for genre in genres:
    print(f"The track number is {counter} which means the genre is {genre}!")
    counter += 1


#Task 2

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
while counter != len(genres):
    print(f"The track number is {counter + 1} which means the genre is {genres[counter]}!")
    counter += 1

    if genres[counter] == "Classical":
        print("Stop at this!")
        break

#Task 3

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for index in range(len(genres)):

    if genres[index] != 'Classical':
        print(f"The track number is {index + 1} and the light show is on!")
    else:
        continue
