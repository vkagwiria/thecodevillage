from grading_systems import grading,total
import math
marks1 = int(input("Enter the marks for the subject : "))
marks2 = int(input("Enter the marks for the subject : "))
marks3= int(input("Enter the marks for the subject : "))
marks4 = int(input("Enter the marks for the subject : "))

grading(marks1)
grading(marks2)
#to import specific functions:
# grading_systems.grading(marks3)
grading(marks4)

total=total(marks1,marks2,marks3,marks4)
print("The total is ", total)

#To find pre-defined variables such as pi: import the module first (import math)
# math.pi
#i.e
print(math.pi)