"""elif statements give us the ability to run separate blocks of code
depending on the condition. They are also known as "else if statements".

elif statements must be associated with an if statement, meaning
that you cannot create an elif without an if. Python works in top to bottom order, so
it checks the first if statement; if that statement is False, it continues to the first elif
statement and checks that condition. If that condition returns False as well, it continues
to the next conditional statement until there are no more to check. However, once a
single conditional statement returns True, all other conditionals are skipped, even if
they are True. It works so that the first conditional to return True is the only block of
code that runs.
"""
# ex
x = 5
y = 10
if x > y:
      print("x is greater")
elif x < y:
      print("x is less")

"""
Checking Multiple Elif Conditions
Having the ability to write multiple decisions based on a single variable is a necessity,
which is why elif statements were built. 
"""
