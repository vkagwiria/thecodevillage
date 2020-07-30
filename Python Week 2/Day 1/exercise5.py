age=int(input("Please enter your age here: "))
if(age<18):
    print("Your are not allowed to proceed.")
elif(18<age<=35):
    print("You are allowed to proceed")
else:
    print("Invalid age. Please try again.")