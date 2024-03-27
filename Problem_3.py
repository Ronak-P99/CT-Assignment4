'''
Objective:
The aim of this assignment is to explore the importance of the loop condition in while loops. 
You will create loops with different conditions to see how they influence the behavior of the loop.

Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be true (an infinite loop). 
Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.

Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. 
The loop should terminate naturally once the condition is met.
'''

#Task 1

count = 0

while count < 100000: 
    if(count < 5):
        print(f"This is iteration: {count}!")
        count += 1
    else:
        print(f"{count} is the final iteration!")
        break


#Task 2

count = 0

while count < 100000: 
    if(count < 5):
        print(f"This is iteration: {count}!")
        count += 1
    else:
        print(f"{count} is the final iteration!")
        count = 500000