# User Input: Ask the user to input the time of day in military time without a
# colon (1100 = 11:00 AM). Write a conditional statement so that it outputs the
# following:
# a. “Good Morning” if less than 1200
# b. “Good Afternoon” if between 1200 and 1700
# c. “Good Evening” if equal or above 1700


time=int(input("Please insert your local time here in millitary hours without spacing, a colon or hrs: "))
if(time<1200):
    print("Good morning!")
elif(1700>time>=1200):
    print("Good afternoon!")
elif(time>=1700):
    print("Good evening!")