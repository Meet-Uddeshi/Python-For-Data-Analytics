# Topic: Strings. Strings are immutable and ordered. It is array of characters.
import string

m = "Hello World"
print(m)
print('''This is mulitiline
strings.''')
print("""This is also
multiline stings.""")

# Strings can be concatenated
m = "Hello"
b = "World"
print(m+b)

# Characters of specific strings can be access by its index
print(m[2])

# String slicing
print(m[0:2]) # It is as same as array. string[starting_index:ending_index:gap/difference]. It takes 0 index, last index and 1 gap or difference by default.

# String functions. These functions are used to string manipulation.
# lower() - to convert all characters in string to lowercase
# upeer() - to convert all characters in string to uppercase
# count() - to count specific character in string
# replace() - to replace character in string
# capitalize - to capital first character of string
# strip() - to trim left and right side both
# lstrip() - to trim only left side in string
# rstrip() - to trim only right side

m.count("o")
m.lower()
m.upper()
m.strip()
print(m)