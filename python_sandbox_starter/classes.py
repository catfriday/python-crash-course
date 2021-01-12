# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#  create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old'

    def has_birthday(self):
        self.age +=1

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}'

#  Initialize User object
brad = User('Brad T.', 'brad@gmail.com', 36)
# Initialize a customer
janet = Customer('Janet J.', 'jan@gamil.com', 25)
janet.set_balance(500)
print(janet.greeting())

# print(type(brad))
# print(brad.name)
# brad.has_birthday()
# print(brad.greeting())
