print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# EVALUATE: returns true if there is some content
print(bool("Hello"))
print(bool(15))
print(bool("")) # this one false
print(bool(False)) # also false
print(bool(None)) # also false
print(bool(())) # also false
print(bool([])) # also false
print(bool({})) # also false

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction2() :
  return True

if myFunction2():
  print("YES, it's true!")
else:
  print("NO, it's false!")

# IS INSTANCE DETERMINES WHETHER VARIABLE IS DATA TYPE OR NOT
x = 200
print(isinstance(x, int))