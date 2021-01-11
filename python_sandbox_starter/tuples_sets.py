# A Tuple is a collection which is ordered and UNCHANGEABLE. Allows duplicate members.
 

#  create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apple', 'Oranges')) constructor way

# If tuple only has one value, you need a comma after
fruits2 = ('Apples',)

# Tuples cannot be changed like below
# fruits[0] = 'Pears'  #will give an error

# Delete a tuple, will give you 'not defined' in terminal if done right
del fruits2

# Get length
print(len(fruits))
# print(fruits2)


# *********SETS************

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_sets = {'Apples', 'Oranges', 'Pears'}

# check if in set will be true or false
print('Apples' in fruits_sets)

# Add to set 
fruits_sets.add('Grape')

# Remove from set
fruits_sets.remove('Grape')

# Clear Set, set will still exist only will be empty
fruits_sets.clear()

# Delete set
del fruits_sets
