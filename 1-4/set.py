### PYTHON SETS

### SET - no order, no change of elements, no duplicates
### True and 1/False and 0 are considered the same thing

myset = {"apple", "banana", "cherry"}
print(myset)
myset2 = {"apple", "apple", "banana", "cherry"}
print(myset2)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(f"Length of thisset is {len(thisset)}")

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(f"Type of set4 {type(set4)}")

### SET constructor: set()
newset = set(("apple", "strawberry", "pineapple")) # note the double round-brackets
print(f"newset is {newset}")

### ACCESS ITEMS (FOR) - Note that the order of looping will be totally random
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

### Check for elements
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("banana" in thisset)
print("zakabra" in thisset)
print("banana" not in thisset)
print("zakabra" not in thisset)

### Add Set Items
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

### Add Set elements to another set
thisset = {"apple", "banana", "cherry"}
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
print(tropical)
thisset.update(tropical)
print(thisset)
thislist= ("list1", "list2")
thisset.update(thislist)
print(thisset)

### Remove element: remove/discard
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
### if no such element, remove produces error; discard does not
thisset.discard("apple")
print(thisset)

### Remove random element: pop
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)

### Empty the set
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.clear()
print(thisset)

### Delete the set: del
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset

### JOINING SETS
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

### UNION
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set4 = set1 | set2 ### SAME as union()
print(set3)
print(set4)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", "bananas" }
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
myset2 = set1 | set2 | set3 | set4
print(myset)
print(myset2)
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

### UPDATE: inserts all elements of the new set into the old set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

### INTERSECTION: keep only duplicates ina new set. Can be replaced with "&"
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana"}
set3 = set1 & set2
print(set3)

### INTERSECTION UPDATE: intersection_update() method will also keep ONLY the duplicates,
### but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

### Once again True/False/1/0 are the same and are treated as duplicates
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

### Difference: will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
### same result with "-" operator
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

### DIFFERENCE UPDATE: will also keep the items from the first set that are not in the other set,
### but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

### SYMMETRIC DIFFERENCE: The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
### same effect by ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

### SYMMETRIC DIFFERENCE UPDATE: method will also keep all but the duplicates,
### but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

### More Methods
set1 = {"apple", "banana", "cherry"}
set2 = set1.copy()
print(set2)
set2 = {"google", "microsoft", "apple"}
set1_part = {"apple", "banana"}
print(set1.isdisjoint(set2)) ## Returns whether two sets have a intersection or not
print(set1.issubset(set2)) ## Returns whether another set contains this set or not
print(set1.issuperset(set2)) ## Returns whether this set contains another set or not

print(set1_part.issuperset(set1)) ## Returns whether this set contains another set or not
print(set1.issuperset(set1_part)) ## Returns whether this set contains another set or not
