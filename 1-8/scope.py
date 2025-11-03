### SCOPE
# A variable is only available from inside the region it is created. This is called scope.

def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc2():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc2()

### GLOBAL SCOPE

x = 300
def myfunc3():
  print(x)
myfunc()

print(x)

x = 500
def myfunc4():
  x = 400
  print(x)
myfunc4()
print(x)

### GLOBAL SCOPE INSIDE LOCAL FUNCTION

def myfunc5():
  global x
  x = 3256
  print(x)
myfunc5()

print(x)

### RE-DEFINE GLOBAL VARIABLE IN LOCAL FUNCTION

x = 256
def myfunc6():
  global x
  x = 257
myfunc6()
print(x)

### NONLOCAL - to work with nested functions, changing value for the OUTER function (myfunc26 to myfunc25, in this case)
def myfunc25():
  x = "Jane"
  def myfunc26():
    nonlocal x
    x = "hello"
  myfunc26()
  return x

print(myfunc25())
