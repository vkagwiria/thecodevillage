# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for units of quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
num=int(input("Please insert the number of items purchased: "))
total=(num*100)
if(total>=1000):
    sale= (total - (total * 0.1))
    print(f"Congratulations! You qualify for a 10% discount. Your total purchase costs Ksh.{sale}.")
elif(0<=total<1000):
    print(f"Sorry, you do not qualify for a discount. Your total purchase costs Ksh.{total}.")
else:
    print("Sorry, please insert the correct number of items purchased.")