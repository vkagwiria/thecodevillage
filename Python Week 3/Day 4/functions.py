# a = 2 # 3
# b = 3 # 5

# # sum = a+ b
# print(sum)

# syntax : def function_name(parameters or arguments):


"""
sandwich - bread, meat, vegetables

bread - brown, white, wholemeal
meat - ham, brawn etc
vegetables - lettuce, cabbage, celery

def sandwich(bread,meat,veggies):
    sandwich = bread + meat + veggies
    return sandwich

sandwich(brown,ham,lettuce) # calling or invoking a function

"""

def sum(a,b):
    sum = a + b
    
    return sum


sum1 = sum(2,3)
sum2 = sum(5,6)
sum3 = sum(7,60)

print(f"Sum 1: {sum1} Sum 2:  {sum2} Sum 3: {sum3}")

# "Hello Nick"


name = input("Enter your name: ")

def greeting(name):
    greeting = "Hello " + name
    return greeting

greeting = greeting(name)

print(greeting)

# product = (sum(4,5) * 3)
# print(product)
