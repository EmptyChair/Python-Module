### CLASSES
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

### INITIALIZATION
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

### RETURN AS STRING
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} of age {self.age}"

p1 = Person("John", 36)

print(p1)

### SOME FUNCTIONS

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def represent(self):
    print(f"Hello my name is {self.name} and I am {self.age} years old.")

p1 = Person("John", 36)
p2 = Person("Gary", 2)
p1.represent()
p2.represent()

### SELF: NO NEED TO BE CALLED "SELF"
class Person:
  def __init__(myOwnObject, name, age):
    myOwnObject.name = name
    myOwnObject.age = age

  def myfunc(abc):
    print(f"Hello my name is {abc.name} and I am {abc.age} years old.")

p1 = Person("John", 36)
p1.myfunc()

### PROPERTY MODIFICATION:
p1.age = 45
p1.myfunc()

### PROPERTY DELETION:
del p1.age
#p1.myfunc()  - will show error cause the age ain't present

### EMPTY CLASS:

class EmptyClass:
  pass