thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(f"length of thistuple is {len(thistuple)}")

# ONE-ITEM TUPLE
thistuple2 = ("apple",)
print(thistuple2)
print(type(thistuple2))

#NOT a tuple
thistuple3 = ("apple")
print(type(thistuple3))

# NO DATA TYPE LIMITATION
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

### TUPLE CONSTRUCTOR:
newtuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(newtuple)

### Access Items of Tuple
thistuple = ("apple", "banana", "cherry")
print(f"The item in position 1 of thistuple is: {thistuple[1]}")

### Negative indexing
print(f"The last item in thistuple is: {thistuple[-1]}")

### Range - first element included, last element NOT included!!!
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"thistuple is {thistuple}")
print(f"Range 2:5 {thistuple[2:5]}")
print(f"Range :4 {thistuple[:4]}")
print(f"Range 1: {thistuple[1:]}")
### NOTE! Negative range: index -4 (included) to index -1 (excluded)
print(f"Range -4:-1 {thistuple[-4:-1]}")
print(f"Range -4: {thistuple[-4:]}")

### Check for item:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
if "bomb" not in thistuple:
  print("No, 'bomb' is NOT in the fruits tuple")

### TUPLE is unchangeable - but you can convert it to list and change it that way
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

### ADD ELEMENT: also convert into a list and back
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

### ADD ELEMENT: merge two tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

### REMOVE ELEMENT: again, list shenanigans
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

### DELETE IT
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

### Packing TUPLE: assign values to it
fruits = ("apple", "banana", "cherry")
print(f"Tuple fruits: {fruits}")

### Unpacking tuple: extract the values back into variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

### Unpack with Asterisk: upacks values into one new value AS A LIST!!!!
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

### LOOPING TUPLES
thistuple = ("apple", "banana", "cherry")
for element in thistuple:
  print(element)
for i in range(len(thistuple)-1): # 1 element less
  print(thistuple[i])
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i +=1

### JOINING TUPLES
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

### MULTIPLY TUPLES
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 5
print(mytuple)

### METHODS:
t1 = ("a", "b" , "c", "ghjdsfog", "suzerain", "bolt", "c")
count = t1.count("c")
print(f"Count of 'c' elemnts in t1 is {count}")
print(f"Index of first 'b' elemnt in t1 is {t1.index("b")}")
