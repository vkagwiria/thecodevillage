"""
# Arithmetic Operators 
## Addition operator +
## Subtraction - 
## Multiplication * 
## Division /
## Modulus %... see if a number divided by another gives a reminder
## Exponent ** .... to raise a number to the power of sth  i.e  2**2 will gives the square of 2 which is 4






# Logical Operators
# Logical Operators
## Logical Operator "and"
"""
"""
Ensures that when you check for multiple conditions, both sides of the condition are True.
This means that if either the condition to the left or right of the “and” is False, 
then the code will not run the block of code.
"""
# ex
# using the keyword 'and' in an 'if statement'
x =5 
y = 10 
z = 5
if x < y and x == z:
      print("Both statements were true")


## Logical Operator "or"
"""
Checks for one or both conditions to be true. Such that if the condition to the left is False 
and the condition to the right is True, the block of code will still run because at least 
one condition was True. The only time an “if block” will not run using an “or” operator is 
when both conditions are False. 
"""
# ex 
# using the keyword 'or' in an 'if statement'
x = 5 
y = 10
z = 5
if x < y or x != z:
      print("One or both statements were true")



## Logical Operator "not"
"""
Checks for the opposite of a value. The “not” operator is used for just that. 

# Assignment Operators
# Bitwise Operators
# Membership Operators

# Comparison Operators
# Equality ==
# Inequality !=
# Greater than >
# Less than <
# Greater than or equal >=
# Less or equal <=

# Membership Operator “in”
"""

"""Used when you want to check if a given object has a value appear in it.
The best use case is checking for a certain value within strings.
"""

# using the keyword 'in' within an 'if statement'
name = "Valentine"
if "tine" in name:
      print(f"tine is in {name}")


# Membership Operator “not in”
"""
If you want to check to see if an object doesn’t include a specific value, you
would use the “not in” operator. This is essentially just checking the opposite of the “in”
operator.
"""
# using the keyword 'not in' within an 'if statement'
if "b" not in name:
      print(f"b is not in {name}")


