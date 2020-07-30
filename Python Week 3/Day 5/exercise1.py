# ask user for a number, which is the radius a circle
# if the number <= 10, calculate the circumference
# if the number is greater than 10, calculate the area
# should have functions for calculating circumference and area
num=int(input("Please insert your radius here: "))
def circumference(num):
    
    circumference= (2*num)* 3.142
     
    return circumference
       

def area(num):
    area=3.142*(num**2)

    return area
if num<=10:
    circumference= circumference(num)
    print("The circumference is ", circumference)
elif num>10:
    area=area(num)
    print("The area is ", area)