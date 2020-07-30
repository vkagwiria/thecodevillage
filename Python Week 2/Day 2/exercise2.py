# ask user for the year of birth
# calculate the current age
# if the age is less than or equal to 1, return "Infancy"
# if the age is greater than 1 but less than or equal to 3, return "Toddlerhood"
# if the age is greater than 3 but less than 13, return "Childhood"
# if the age is greater than or equal to 13 but less than or equal to 19, return "Adolescence"
# else, return "Adult"
year=int(input("Please insert your year of birth: "))
age=int(2020 - year)
if (age<=1):
    print("Infancy")
elif(3>=age>1):
    print("Toddlerhood")
elif(13>age>3):
    print("Childhood")
elif(19>=age>=13):
    print("Adolescence")
else:
    print("Adulthood")