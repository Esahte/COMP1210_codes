from re import *

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# Find people with first and last name only
regex = '^\w+ \w+$'
for name in names:
    result = search(regex, name)
    if result:
        print(name)