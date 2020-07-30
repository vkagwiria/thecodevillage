"""
An object is how we reference real world items.

Object Oriented Programming
Objects in Python are created from classes. The point of OOP is to reuse the same code
while giving flexibility to create each object with their own features.

Stages of OOP

First stage is the class definition. This is where you write the blueprint to be used when called.
The second stage is called instantiation. It is the process of creating an object from the
class definition. After an object is instantiated, it is known as an instance. You may have
multiple instances from a single class definition.


Car - base/blueprint            
- ford
- toyota
- mazda
- lambos

Person - base
- race
- weight
- height
"""
# creating and instantiating a class
# class definition
class Car():
    pass # placeholder


ford = Car() # creates an instance of the Car class and stores it in the variable ford
toyota = Car()


# attributes (variables within a class)
# methods (functions within a class)
# inheritance (parent or base classes)
