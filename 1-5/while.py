### WHILE LOOP
i = 1
while i < 6:
  print(i)
  i += 1

### BREAK
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

### CONTINUE - can stop the current iteration, and continue with the next:
## effectively passes the iteration i == 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

### WHILE-ELSE
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")














