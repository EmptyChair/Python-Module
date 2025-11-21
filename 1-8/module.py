# IMPORT MODULE

import test_module

test_module.greeting("Anton")
print("Person1's age is...")
print(test_module.person1["age"])

# Import module and create and alias:

import test_module as mymodule

a = mymodule.person1["name"]
print("name of person1 is "+a)

# BUILT IN MODULE - platform

import platform

x = platform.system()
print(x)

# DIR() function to list all names/variable names

x = dir(platform)
print(x)

y= dir(mymodule)
print(y)

from test_module import person1
print("Age of person1 is...")
print(person1["age"])