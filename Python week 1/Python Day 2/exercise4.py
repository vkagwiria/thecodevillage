firstname = input("Please insert your first name: ")
lastname = input("Please insert your last name: ")
identity = input("Please insert your ID number: ")
firstno = int(input("Please insert your first number here: "))
lastno = int(input("Please insert your last number here: "))
sum = firstno + lastno
print("Hi,", firstname, lastname,".", "Your identity number is", identity, ".", "The sum of your numbers is", sum, ".")
print("Hi,{} {}. Your ID number is {}. The sum of your numbers is {}".format(firstname, lastname, identity, sum))
print(f"Hi,{firstname} {lastname}. Your identity number is {identity} and the sum of your numbers is {sum}.")