print("hello")
print('hello')

# QUOTES - use unmatched quotes
print("He is called 'Johnny'")
print('He is called "Johnny"')

# ASSIGN STRING
s1 = "hello my"
print(s1)

# MULTILINE STRING (like multiline comment)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# take 2nd character of a (Lorem)
print(a[1])

# LOOP THROUGH STRING:
for x in "banana":
    print(x)

# LENGTH
b = "dfgsdfgsdfg"
print(len(b))

txt = "I gotta break free!"
print("free" in txt)
print("bungaloo" in txt)
if "free" in txt:
    print("There is  'free' in txt text")

print("cheap" in txt)
if "cheap" not in txt:
    print("There is no 'cheap' in txt text")

# SLICING
str1 = "My great grandmother"
print(str1[3:8])
print(str1[:8])
print(str1[3:])
print(str1[-11:])

# UPPER CASE
str2 = str1.upper()
print(str2)

# LOWER CASE
str3 = str2.lower()
print(str3)

# WHITE SPACE REMOVAL
str4 = " My neko has no claws! "
print(str4)
print(str4.strip())

# REPLACE STRING
str5 = str4.replace("My", "Your")
print(str5)

# SPLIT STRING
print(str5.split("has"))
[start, end] = str5.split("has")
print(start)
print(end)

# CONCATENATE
print((start+"has"+end).strip())

# F-STRINGS
age = 36
txt = f"My name is Harry and I am {age}"
print(txt)

# PLACEHOLDER/MODIFIER
price = 59
txt = f"The price is {price:.5f} dollars"
print(txt)
txt2 = f"But for you, the price is {20 * price:.5f} dollars"
print(txt2)

# ESCAPE CHARACTER
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

##\' 	Single Quote
#\\ 	Backslash
#\n 	New Line
#\r 	Carriage Return
#\t 	Tab
#\b 	Backspace
#\f 	Form Feed
#\ooo 	Octal value
#\xhh 	Hex value


# STRING METHODS
'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
