# Create a class, Person. Ask the user to input their name, address and email 
# and create an instance of the Person class with the details given.
# Print out their details.

class person():
    def __init__(self, name, address, email):
        self.name=name
        self.address=address
        self.email=email

name=input("Please insert your name: ")
address=input("Please insert your address: ")
email=input("Please insert your email: ")

person1=person(name, address, email)

print(person1.name, person1.address, person1.email)