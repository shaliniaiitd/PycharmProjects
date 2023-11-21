import re

print(help(re))
#Help on package re:

# NAME
#     re - Support for regular expressions (RE).
#
# MODULE REFERENCE
#     https://docs.python.org/3.11/library/re.html
#\d  is a special sequence that matches any digit between 0 to 9.

s  = "My age is 34"

print(re.findall('\d',s))

#print("without raw string:")
# path_to_search = "c:\example\task\new" - > gives error.

#with raw string
target_string = r"c:\example\task\new\exercises\session1"

# regex pattern
pattern = r"^c:\\example\\task\\new"
# \n and \t has a special meaning in Python
# Python will treat them differently
res = re.search(pattern, target_string)
print(res.group())


target_string = "Jessa salary is 8000$"

# compile regex pattern
# pattern to match any character
str_pattern = r"\w"
pattern = re.compile(str_pattern)

# match regex pattern at start of the string
res = pattern.match(target_string)
# match character
print(res.group())
# Output 'J'

# search regex pattern anywhere inside string
# pattern to search any digit
res = re.search(r"\d", target_string)
print(res.group())
# Output 8

# pattern to find all digits
res = re.findall(r"\d", target_string)
print(res)
# Output ['8', '0', '0', '0']

# regex to split string on whitespaces
res = re.split(r"\s", target_string)
print("All tokens:", res)
# Output ['Jessa', 'salary', 'is', '8000$']

# regex for replacement
# replace space with hyphen
res = re.sub(r"\s", "-", target_string)
# string after replacement:
print(res)
# Output Jessa-salary-is-8000$