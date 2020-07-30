# Ask the user for 3 numbers
# Calculate the sum of the three numbers
# if the values are equal then return thrice of their sum
# else, return the sum

num1=int(input("Please insert the first number here: "))
num2=int(input("Please insert the second number here: "))
num3=int(input("Please insert the third number here: "))
sum=num1+num2+num3
if(num1==num2==num3):
    print(f"The sum of your numbers is {3*sum}.")
else:
    print(f"The sum is {sum}.")