# Loops
"""
Loops in Python - "for loop" and "while loop"
Loops allow us to rerun the same lines of code several times. 
Loops will always run until a condition is met.

"""
# For Loop - used to loop a set number of times
"""
syntax:
for num in range(5):

range(start,stop,step) (0,100,2)
range(0,5,1)

for - keyword that begins loop
num - temp variable, also known as counter or index
in - keyword
range function - allows us to count from one number to another while being able to define
the start and end
"""
# ex 
for num in range(5): # range counts up to but not including
    print(f"Value: {num}")

for i in range(0,100,2):
    print(i)

for j in range(0,100,5):
    print(j)

# Looping By Element strings, lists, dictionaries, sets
"""
When working with data types that are iterable, meaning they have a collection of
elements that can be looped over, we can write the for loop differently:
"""

name = "John Smith"
for letter in name:
    print(f"Value: {letter}")



# Continue Statement
"""
Once a continue statement is hit, the current iteration stops and goes back to the top of
the loop.
# """


for num in range(7):
    if num == 3:
        continue
    print(num)



# Break Statement
"""
It allows us to break out of a loop at any point in time 
# """
for num in range(5):
    if num == 3:
        break
    print(num)
    


# Pass Statement
"""
The pass statement is simply just a placeholder so that the program does not break
"""
for i in range(5):
    # TODO: add code to print number
    pass
    
    

"""
Note: Using "TODO" is a general practice for setting a reminder
"""


# Nested loop (x,y)

"""
A loop within a loop. When using nested loops, the inner loop must always finish 
"""