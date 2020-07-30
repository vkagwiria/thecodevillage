"""
A dictionary is a collection of unordered data, which is stored in key-value pairs. What
is meant by “unordered” is the way it is stored in memory. It is not accessible through
an index, rather it is accessed through a key.
"""
# empty
my_dictionary = {}
# a dictionary with two key-value pairs
person = {
    'name':'Morty',
    'age': 20
}

# declare using constructor
person2 = dict(first_name="Valentine",age=23)

# access 
print(person['name'])

# access using .get method
print(person.get('age'))

# add key/value pair
person['address'] = 'Mombasa'

print(person)

# access keys
print(person.keys())
# access values
print(person.values())

# remove key-value pair - del() or pop()
# del(person['age'])
person.pop('age')
print(person)

# clear
person.clear()
print(person)

# check length/ number of key-value pairs
print(len(person2))

# lists in dictionaries
cities = {
    'African': ['Nairobi','Kigali', 'Bujumbura'],
    'European': ['Helsinki','Prague']
}

print(cities['European'][1])

print(cities['European'])

# copy - .copy()

person_clone = person.copy()
name_of_dictionary_copy = name_of_dictionary.copy()
print(person_clone)
print(name_of_dictionary_copy)

# looping through a dictionary

# keys only
for key in name_of_dictionary.keys():
    print(key)
# # values only
for value in name_of_dictionary.values():
    print(value)
# # key - value pairs
for key, value in name_of_dictionary.items():
    print(key, value)