# Ask the user to input a number
# Check if number is greater than 100 and less than 300
# if number is greater than 100 and less than 300, check if the number is even
# print "Number is even"

num = int(input("Please insert your number here: "))
if (num<300 and num>100): 
    num %2 == 0
    print("The number is even.")