import random

choices=["rock", "paper", "scissors"]
x=(random.choice(choices))
y=input("Rock, paper, scissors? ").lower()

if (x=="rock" and y=="rock") or (x=="rock" and y=="scissors") or (x=="paper" and y=="rock") or (x=="paper" and y=="paper") or (x=="scissors" and y=="scissors") or (x=="scissors" and y=="paper"):
    print(f"My choice: {x}")
    print(f"Your Choice: {y}")
    print("Sorry, try again.")
elif (x=="rock" and y=="paper") or (x=="paper" and y=="scissors") or (x=="scissors" and y=="rock"):
    print(f"My choice: {x}")
    print(f"Your Choice: {y}")
    print("Awesome, you won!")
else:
    print("Sorry, choose from rock, paper and scissors!")