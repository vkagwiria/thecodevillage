# ask user for two numbers
# check if the first number is greater than the second number
# if the first number is greater, print "The number 3 is greater than 2"
# if the first number is lower, print "The number 2 is lower than 3"
# if the numbers are equal, print "Both numbers are equal"

num1=int(input("Please insert your first number here: "))
num2=int(input("Please insert your second number here: "))
if(num1>num2):
    print(f"Your first number {num1} is greater than the second number {num2}.")
elif(num1<num2):
    print(f"Your first number {num1} is less than the second number {num2}.")
elif(num1==num2):
    print("Both numbers are equal. ")