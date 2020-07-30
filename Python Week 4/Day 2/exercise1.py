# ask user for radius
# use a lambda function to calculate the area

area =lambda radius: radius*radius*3.142
radius = int(input("Please insert the radius here: "))

print("The area is", area(radius))
