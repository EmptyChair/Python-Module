### JSON and Python
### Don't name file json.py, or it will confuse parser!

import json

### If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

### If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

### You can convert Python objects of the following types, into JSON strings:
'''
    dict
    list
    tuple
    string
    int
    float
    True
    False
    None
'''

# Convert Python objects into JSON strings, and print the values:

print("Example")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

'''
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
'''

test1 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(" print test 1: "+json.dumps(test1))

## same with indents to make output look prettier:
print(" print test 1 with indents: "+json.dumps(test1,indent=3))
# Use the separators parameter to change the default separator:
print(" print test 1 with new separators: "+json.dumps(test1, indent=4, separators=(". ", " = ")))
# The json.dumps() method has parameters to order the keys in the result:
print(" print test 1 with new separators and sorting by key: "+ json.dumps(test1, indent=4, sort_keys=True))



