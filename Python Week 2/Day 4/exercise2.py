# user inputs a number 
# print its multiplication table


number = int(input("Please insert your number here: "))
for num in range (0,11):
    product = num * number
    print(f"The product of {number} and {num} is {product}.")