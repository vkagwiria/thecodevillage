# Functions with default parameters
def sayHello(name="John"):
    return f'Hello {name}'

print(sayHello())

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

result = getSum(4,9)
print(result)


# anonymous functions/lambda functions
"""
An anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, 
anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.

syntax:

lambda arguments: expression

Note: Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned.

"""

sum = lambda number1,number2: number1 + number2
print(sum(5,6))
