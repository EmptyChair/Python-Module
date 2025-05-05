mylist = ["apple", "banana", "cherry"]
mylist1 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
print(mylist)
print(mylist1)

a = len(mylist)
# f-string
print(f"Length of mylist is {a}")

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

list5 = list(("apple", "orange"))
print(f"List five contains {list5}")
print(list5[1])

list6 = [0,1,2,3,4,5,6,7,8,9,10]
print(list6[0])
print(list6[1])
print(list6[2])
print(list6[-1])
print(list6[-2])
print(list6[-3])
# End point not included!
print(list6[1:6])
print(list6[:3])
print(list6[3:])
print(list6[-3:])
print(list6[-3:-1])

if 10 in list6:
    print("Yes, there is 10 in list6")

list6[1] = "blackcurrant"
print(list6)
# insert 2 elements in place of 2 elements
list6[1:3] = ["blackcurrant", "boom", ]
print(list6)
# insert 2 elements in place of 8 elements - removes the rest
list6[1:9] = ["blackcurrant", "boom", ]
print(list6)
# insert element in third position, rest shifts
list6.insert(2, "inserted third element")
print(list6)

mylist25 = ['apple', 'banana', 'cherry']
mylist25[1:2] = ['kiwi', 'mango']
print(mylist25)

mylist25.append("doom")
print(mylist25)

mylist26 = ["little doom", "death"]
mylist25.extend(mylist26)
print(mylist25)

mytuple = ("burning", "hanging")
mylist25.extend(mytuple)
print(mylist25)

mylist100 = ["book", "chair", "book", "table", "shelf", "chair"]
mylist100.remove("book")
print(mylist100)
mylist100.pop(-2)
print(mylist100)
del mylist100[0]
print(mylist100)
mylist100.insert(0,"book")
print(mylist100)
mylist100.clear()
print(mylist100)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(f"Element {x} of thisList")
for i in range(len(thislist)):
  print(f"Element {i} of thisList is {thislist[i]}")

c = 0
while c < len(thislist):
  print(thislist[c])
  #c = c+1
  c +=1

thislist2 = ["apple", "banana", "cherry"]
[print(x) for x in thislist2]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print("Newly appended list:")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits if "c" in x]

print(newlist2)

# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10)]

print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits if "k" in x]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# sort is case sensitive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.upper)
print(thislist)

thislist = [item.upper() for item in thislist]
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# COPYING
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

### Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

## need to take inidividual elements, not pack list2 as an element of list 1
for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

list1 = ["a", "b" , "c", 1, 2, 3, 3]
list4 = list1.copy()
print(list4)
list4.append("z")
print(list4)
c1 = list4.count(3)
print(c1)
c2 = list4.index("a")
print(c2)
list4.insert(2, "boom")
print(list4)
list4.remove( "b")
print(list4)
list4.reverse()
print(list4)
#list4.sort()
#print(list4)
list4.clear()
print(list4)



