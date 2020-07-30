import random

x=(random.randint(0, 21))
y=int(input("Take a wild guess! Please insert a number between 0 to 20: "))
a=x-y
b=y-x
if 0<=y<=20:   
    if x==y:
        print(f"You are correct! The number is{x}")
    elif x>y:
        print(f"Sorry, your guess lower by {a}. The correct number is {x}. Try again!")
    elif x<y:
        print(f"Sorry, your guess is higher by {b}. The correct number is {x}. Try again!")
else:
    print("Sorry, try again with a number between 0 and 20.")
