# Task
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format

# A single line containing a positive integer,

# .

# Constraints
# 1<=n<+100

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

num=int(input("Please input a number in single line containing a positive integer: "))
    
if 2<=num<=5 and num%2==0:
    print("Not weird")
        
elif 6<=num<=20 and num%2==0:
    print("Okay")

elif 20<num<=100 and num%2==0:
    print("Not weird")
    
elif num%2!=0 and num<=100:
     print ("Weird")
else:
    print("Invalid")