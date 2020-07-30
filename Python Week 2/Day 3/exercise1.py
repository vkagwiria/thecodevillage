# weight converter - kilos to pounds
# ask the user for their weight
# ask which unit of weight they'd like to convert to
# convert the weight then output with appropriate units i.e 70 kilos or 200 pounds
 
# from kilos to pounds
# /0.45
# from pounds to kilos
# *0.45
weight=int(input("Hello, please insert your weight here: (P or K ) "))
convert=input("Would you like to convert your weight to pounds or kilograms? ")
if(convert.upper() == "P"):
    final = (weight / 0.45)
    print(f"Your weight is {final} lbs.")
elif(convert.upper() == "K"):
    final = weight * 0.45
    print(f"Your weight is {final} kgs.")
else:
    print("Sorry, please try again. ")