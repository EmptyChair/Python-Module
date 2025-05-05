### FOR

### LOOP THROUGH LIST
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

### LOOP THROUGH LETTERS - this only works with ITERABLE OBJECTS!!!
for x in "banana":
  print(x)

### FOR with BREAK
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

### FOR with CONTINUE
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

### FOR with RANGE - from 0 to 5. FIVE, NOT SIX!!!
for x in range(6):
  print(x)

### FOR with RANGE - from 1 to 5. FIVE, NOT SIX!!!
for x in range(1,6):
  print(x)

### FOR with RANGE and INCREMENT - from 2 to 29, increment 3
for x in range(2,30,3):
  print(x)

### FOR and ELSE - else comes into play when for ends
for x in range(2,60,8):
  print(x)
else:
  print("Finally finished!")

### FOR and ELSE and BREAK:
### In Python, the else block in a for loop executes only if the loop completes without encountering a break statement.
### hence else will never come into play
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

### NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

### PASS: for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error
for x in [0, 1, 2]:
  pass

for xxx in range(1080, 1096):
    print(f"command = {{ trigger = {{ NOT = {{ participant = {{ country = PER value = 3 }} }} owned = {{ province = {xxx} data = -3 }} }} type = secedeprovince which = PER value = {xxx} when = 2 }}")
