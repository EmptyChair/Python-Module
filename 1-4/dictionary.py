### DICTIONARIES
# Dictionaries are used to store data values in key:value pairs.#
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))

### NO DUPLICATES
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

### DIFFERENT DATA TYPES
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

### LENGTH and TYPE
print(len(thisdict))
print(type(thisdict))

### DICTIONARY CONSTRUCTOR
newdict = dict(name = "John", age = 40, country = "Great Britain")
print(thisdict)

### ACCESS ITEM BY KEY
print(thisdict["brand"])
x = thisdict.get("brand")
print(x)

### ACCESS ALL KEYS
x = thisdict.keys()
print(thisdict.keys())
print(x)

### UPDATE KEYS AND THEY'LL CHANGE IN THE STORED VARIABLE (REAL-TIME TRACKING, SON!!!)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

### ACCESS VALUES
x = car.values()
print(x)

### CHANGE VALUE AND THEY'LL CHANGE IN THE STORED VARIABLE (REAL-TIME TRACKING, SON!!!)
car["year"] = 2020
print(x)

### GET ITEMS
x = thisdict.items()

### CHANGE ITEMS AND THEY'LL CHANGE IN THE STORED VARIABLE (REAL-TIME TRACKING, SON!!!)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

### CHECK FOR A PARTICULAR KEY
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
if "color" not in thisdict:
    print("No, color is not one of they keys in this dictionary")

### CHANGE VALUES
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

### UPDATE DICTIONARY: update()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

### ADDING ITEMS - by assigning a new index key with value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["color"] = "red"
print(thisdict)

### ADDING ITEMS - by using update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({" maxspeed": "120 kmh"})
print(thisdict)

### REMOVE ITEMS: pop() method - remove item with given key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.pop("model")
thisdict.pop("year")
print(thisdict)

### REMOVE ITEMS: popitem() method - remove last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"max_speed": 120, "gearbox": "automatic"})
print(thisdict)
thisdict.popitem()
print(thisdict)

### DELETE CONTENTS: del
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
del thisdict["model"]
print(thisdict)

### CLEAR CONTENTS: clear
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.clear()
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

### LOOPING
print("Looping through dict")
for x in thisdict:
  print(x)
### LOOPING VALUES
print("Looping through dict values")
for x in thisdict:
  print(thisdict[x])
print("Looping through dict values again")
for x in thisdict.values():
  print(x)
### LOOPING KEYS
print("Looping through dict keys")
for x in thisdict.keys():
  print(x)
### LOOPING KEYS AND VALUES
print("Looping through dict values/keys")
for x, y in thisdict.items():
  print(x, y)

### COPYING DICTIONARY
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
mydict = thisdict.copy()
print(mydict)
mydict2 = dict(thisdict)
print(mydict2)

### NESTED DICTIONARY - create from scratch
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

### NESTED DICTIONARY - merge dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily2)

### ACEES ITEMS INSIDE NESTED DICTIONARIES
print(myfamily["child2"]["name"])
print(myfamily2["child1"]["year"])

### LOOP THOUGH NESTED DICTIONARIES
for x, obj in myfamily.items():
    print(x)
    for y in obj:
      print(y + ':', obj[y])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2 =	{
  "brand": "Ford",
  "year": 1964
}
### OTHER METHODS - fromkeys() - Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict3 = dict.fromkeys(x, y)
print(thisdict3)
### OTHER METHODS - setdefault() - Returns the value of the specified key.
### If the key does not exist: insert the key, with the specified value
x = thisdict.setdefault("model", "Bronco")
print(x)
x = thisdict2.setdefault("model", "Bronco")
print(x)
