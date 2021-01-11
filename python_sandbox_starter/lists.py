# A List is a collection which is ordered and changeable. Allows duplicate members.

#  Create list
numbers = [1,2, 3, 4]
fruits = ['Apples', 'Oranges', 'Grapes']

#  Use a constructor
number2 = list((1, 2, 3, 4))

# Get length below
print(len(fruits))

print(fruits[1])

# Append to a list
fruits.append("Mangos")

# Remove form list
fruits.remove("Grapes")

#  Insert into list by position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverser the array 
fruits.reverse()

# Sort list
fruits.sort()

# Reverse Sort 
fruits.sort(reverse=True)

print(fruits)