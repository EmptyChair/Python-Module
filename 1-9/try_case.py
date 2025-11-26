### try case

'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

'''

try:
  print(x)
except:
  print("An exception occurred") # because x undefined

### Many exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

### try-except-else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Everything went great")

### try-except-else-finally (executes regardless whether error was caught)
try:
  print("Hello")
  print(x)
except:
  print("Something went wrong")
else:
  print("Everything went great")
finally:
    print("Fart noises")

### another example: open file, write, close file regardless whether it worked
print("try writing file...")
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

### raise - raise exception
y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed for y")

x = -1

if x<0:
    raise Exception("X can't be lower than zero")



