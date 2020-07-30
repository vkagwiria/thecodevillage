# Take values of length and breadth of a rectangle from user and check if it is a square or a rectangle.

length=int(input("Please insert the length here: "))
width = int(input("Please insert the width here: "))
if(length==width):
    print("This is a square.")
elif(length!=width):
    print("This is a rectangle.")