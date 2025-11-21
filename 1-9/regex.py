### REGEX - regular expression, search pattern

import re

txt = "The rain in Spain"
# search txt if it starts with "the" and ends with "Spain"
x = re.search("^The.*Spain$", txt)
print(x)

r"""
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string
"""
#fdsaf
r"""
[] 	A set of characters 	"[a-m]" 	
\ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
. 	Any character (except newline character) 	"he..o" 	
^ 	Starts with 	"^hello" 	
$ 	Ends with 	"planet$" 	
* 	Zero or more occurrences 	"he.*o" 	
+ 	One or more occurrences 	"he.+o" 	
? 	Zero or one occurrences 	"he.?o" 	
{} 	Exactly the specified number of occurrences 	"he.{2}o" 	
| 	Either or 	"falls|stays" 	
() 	Capture and group 	 
"""
#fdsaf
"""
re.ASCII 	re.A 	Returns only ASCII matches 	
re.DEBUG 		Returns debug information 	
re.DOTALL 	re.S 	Makes the . character match all characters (including newline character) 	
re.IGNORECASE 	re.I 	Case-insensitive matching 	
re.MULTILINE 	re.M 	Returns only matches at the beginning of each line 	
re.NOFLAG 		Specifies that no flag is set for this pattern 	
re.UNICODE 	re.U 	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches 	
re.VERBOSE 	re.X 	Allows whitespaces and comments inside patterns. Makes the pattern more readable
"""

#fdsaf
r"""
\A 	Returns a match if the specified characters are at the beginning of the string 	"\AThe" 	
\b 	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\bain" or r"ain\b" 	


\B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\Bain"

r"ain\B" 	


\d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d" 	
\D 	Returns a match where the string DOES NOT contain digits 	"\D" 	
\s 	Returns a match where the string contains a white space character 	"\s" 	
\S 	Returns a match where the string DOES NOT contain a white space character 	"\S" 	
\w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w" 	
\W 	Returns a match where the string DOES NOT contain any word characters 	"\W" 	
\Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z"
"""
#fdsaf
r"""
[arn] 	Returns a match where one of the specified characters (a, r, or n) is present 	
[a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
[^arn] 	Returns a match for any character EXCEPT a, r, and n 	
[0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
[0-9] 	Returns a match for any digit between 0 and 9 	
[0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
[+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

### findall() - list of all matches:

txt2 = "The rain in Spain"
txt3 = "The sun in France"
x = re.findall("ai", txt2)
y = re.findall("ai", txt3)
print(x)
print(y)

### The search() function searches the string for a match, and returns a Match object if there is a match.
### If there is more than one match, only the first occurrence of the match will be returned:

### use r"\s" (raw string) to avoid Python escape problems

txt4 = "The rain in Spain"
x = re.search(r"\s", txt4)
y = re.search(" S", txt4)
z = re.search("DE", txt4)
zresult = z.start() if z else -1
print("The first white-space character is located in position:", x.start())
print("The first white-space-big-S combo is located in position:", y.start())
print("The first DE combo is located in position:", zresult)

### The split() function returns a list where the string has been split at each match:
txt5 = "The rain in France"
x = re.split(r"\s", txt5)
print(x)
# maxsplit parameter to limit the amount of splits
y = re.split(r"\s", txt5,2)
print(y)

### The sub() function replaces the matches with the text of your choice:
txt = "The rain in Andes"
x = re.sub(r"\s", " !!! ", txt)
print(x)
# count parameter to control the amount of replacements
x = re.sub(r"\s", " !!! ", txt,2)
print(x)

### A Match Object is an object containing information about the search and the result
txt = "The rain in Spain and Alsaise-Lorraine"
x = re.search("ai", txt) # x ist object
print(x)
print(x.start())
# <re.Match object; span=(5, 7), match='ai'>
#.span() returns a tuple containing the start-, and end positions of the match.
print(x.span())
#.string returns the string passed into the function
print(x.string)
#.group() returns the part of the string where there was a match
print(x.group())


