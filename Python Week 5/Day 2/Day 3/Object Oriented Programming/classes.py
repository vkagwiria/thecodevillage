# attributes (variables within a class)
# class Car():
#     capacity = 2000
#     colour = 'white'

# mazda = Car()
# print(mazda.capacity,mazda.colour)


# # methods (functions within a class)
# class Dog():
#     def bark():
#         return bark

# german_shepherd = Dog()
# # access methods
# german_shepherd.bark()

# using init method
class Car():
    # initialization function or constructor method
    # self keyword refers to the current instance of the class
    def __init__(self,color,capacity): 
        self.color = color
        self.capacity = capacity

# create an instance - an instance of a class is an object
toyota = Car("red",2000)
toyota1 = Car("white",1500)
mazda = Car("grey",1800)


print(toyota.color)
print(toyota1.capacity)
print(mazda.color)

