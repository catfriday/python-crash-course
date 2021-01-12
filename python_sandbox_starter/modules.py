# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date # importing the date from datetime
import time 
from time import time # importing time from time module easier way

# pip modules
from camelcase import CamelCase

# Import custom module
# import validator  one way to do it
from validator import validate_email


# today = datetime.date.today()
# today = date.today()
# timestamp = time.time() # if only used import time
timestamp = time() # if you do from time import
# print(timestamp)

c = CamelCase()
# print(CamelCase().hump('hello there world'))

email = 'test#test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
