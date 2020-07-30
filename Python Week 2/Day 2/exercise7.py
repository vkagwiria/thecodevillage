# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held (Assume total number of classes to be 30)
# Number of classes attended.
# And print:
## percentage of class attended
## Is student is allowed to sit in exam or not.

held= 30
attended = int(input("Please insert the correct number of classes attended: "))
attendance= ((attended)/held) * 100
if (100>=attendance>=75):
    print(f"You have attended {attendance}% of the classes held this semester. You are eligible to sit the end of sememster exams.")
elif(0<=attendance<75):
    print(f"You have attended {attendance}% of the classes held this semester. Sorry, you are not eligible to sit the end of semester exams.")
else:
    print("Sorry, please try again.")