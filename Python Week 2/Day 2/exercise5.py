# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks=int(input("Please insert your marks out of a hundred: "))
if(marks<25):
    print("F")
elif(45>marks>=25):
    print("E")
elif(50>=marks>=45):
    print("D")
elif(60>marks>=50):
    print("C")
elif(80>marks>=60):
    print("B")
elif(100>=marks>=80):
    print("A")
else:
    print("Sorry, please insert a valid number. ")
