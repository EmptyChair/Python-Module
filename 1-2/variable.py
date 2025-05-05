x = 5
y = "John"
z = 'John' #same as y

print(x, y, z)

x = "Voom"

print(x, y, z)

# Casting

a = str(3)
b = int(3)
c = float(3)

print(a,b,c)
print(a, type(a))
print(b, type(b))
print(c, type(c))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a = b = c = "Forbidden"
print(a,b,c)

suicide = ["hanging", "shooting", "poisoning"]
m,l,n = suicide
print("Suicide types: "+m,l,n)

a = 1
b =2
print(a+b)
a = "tree"
b = " yellow"
print(a+b)

x = "great"

def myfunc():
        x = "not so great"
        print("Launching myfunc...")
        print("Python is "+x)
        print("Complete!")
myfunc()
print("Use global x")
print("Python is "+x)


def myfunc1():
    global x1
    x1 = "abominable"
    print("Launching myfunc...")
    print("Python is " + x1)
    print("Complete!")


myfunc1()
print("Use global x1")
print("Python is "+x1)

