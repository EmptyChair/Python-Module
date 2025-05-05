#### NO ARRAYS - USE LISTS AS ARRAYS
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print("1st element of cars "+x)

### MODIFY ARRAY
cars[0] = "Toyota"
print("1st element of cars "+cars[0])

### LENGTH
x = len(cars)
print(f"Length of cars is {len(cars)}")

### LOOP
for x in cars:
  print(x)

### ADD ELEMENT
cars.append("Honda")

### Remove ELEMENT (2nd one)
cars.pop(1)
for x in cars:
  print(x)

### Remove ELEMENT (specified)
cars.remove("BMW")

### EXTEND
cars.extend("Boomer")
for x in cars:
  print(x)

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

