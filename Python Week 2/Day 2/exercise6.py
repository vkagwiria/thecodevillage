# Take input of age of 3 people by user and determine oldest and youngest among them
age1=int(input("Please insert the first age here: "))
age2=int(input("Please insert the second age here: "))
age3=int(input("Please insert the third age here: "))
if(age1>age2 and age2>age3 and age1>age3 ):
    print(f"{age1} is the oldest and {age3} is the youngest. ")
elif(age1<age2 and age2>age3 and age1<age3):
    print(f"{age2} is the oldest and {age1} is the youngest ")
elif(age1<age3 and age2<age3 and age2>age1):
    print(f"{age3} is the oldest and {age1} is the youngest")
elif(age1==age2==age3):
    print("All are the same age.")
else:
    print("Sorry, please insert three ages")