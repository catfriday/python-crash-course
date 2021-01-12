# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictionary
person ={
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

# Use Constructor
# person2 = dict(first_name='Sare', last_name='Williams')

# Add value to dict
person['phone'] = '555-5577'


# Get All Dict Keyys
# print(person.keys())

# Get Items
# print(person.items())

# Copy a dict SIMILAR TO SPREAD OPERATOR
person3 = person.copy()
person3['city'] = 'Boston'
# print(person3)


# Remove item
del(person['age'])
person.pop('phone')
# print(person)

# Clear Dict
person.clear()

# Get Length
# print(len(person3))

# List of Dicts
people = [
    {'name' : 'Martha', 'age' : 30},
    {'name' : 'Kevin', 'age' : 35}
]
print(people[0]['name'])


#### Get Value #### 
# print(person['first_name'])
# print(person, type(person))
# print(person.get('last_name'))
# print(person)