# Ask the user for their name and age, and then create a dictionary 
# with those key-value pairs. Output the dictionary once created.

details={

    'name': input("Please insert your name here: "),
    'age': int(input("Please insert your age here:"))
}

print(details['name'], details['age'])