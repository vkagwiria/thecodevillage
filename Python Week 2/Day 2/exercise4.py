# A company decided to give bonus of 5% to its employees if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Please insert your salary in numbers: "))
hired=int(input("Please insert the year you were hired: "))
service=(2020-hired)
bonus= int(salary * 0.05)
if(service>=5):
    print(f"Your net bonus amount is {bonus}.")
elif(service<5):
    print("Sorry, you don't qualify for a bonus.")