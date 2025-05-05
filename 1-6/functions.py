### FUNCTION

def my_function():
  print("Hello from a function")

my_function()

### ARGUMENTS/PARAMETERS
def my_function(fname):
  print(fname + " Butakal")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

### MULTIPLE ARGUMENTS

def my_function(fname, lname):
  print("His name is "+fname + " " + lname)

my_function("Emil", "Refsnes")

### ARBITRARY ARGUMENTS - sends multiple arguments in a tuple
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

### KEYWORD ARGUMENTS - purely syntax
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

### COMBINATION: Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

### DEFAULT PARAMETER VALUE
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

### LIST AS ARGUMENT
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

### RETURN VALUES
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

### PASS: if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
    pass

### POSITIONAL ONLY ARGS
def my_function(x, /):
  print(x)

my_function(3)
#my_function(x = 3) - will give error

### KEYWORD ONLY ARGS
def my_function(*, x):
  print(x)

my_function(x = 3)
#my_function(3) - will give error

### Combine Positional-Only and Keyword-Only
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

### RECURSION
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)