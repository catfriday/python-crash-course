# Python has functions for creating, reading, updating, and deleting files.
# open a file/create a file. It will pop up in files when you run this file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name:', myFile.name)
print('Is Closed:', myFile.closed)
print('Opening Mode:', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write('and Javascript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write('and Casey')
myFile.close()

# Read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
