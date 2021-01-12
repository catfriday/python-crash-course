# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create function
def sayHello(name= 'Friday'):
    print(f'Hello {name}')

# sayHello()

# Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total
# print(getSum(3, 4))
num = getSum(3,7)
# print(num)



#***** A LAMBDA function is a small anonymous function. Sort of like an arrow function in javascript. Will implicitly return value
getSum = lambda num1, num2 : num1 + num2 
print(getSum(10, 3))
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

