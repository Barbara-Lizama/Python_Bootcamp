## The string module in Python provides a collection of utilities that can be used for common string operations. To use this module, you'll need to import it first.
# Importing the string module and exploring constants
import string
print(string.ascii_letters) ## alphabet lower and upper
print(string.ascii_lowercase)   
print(string.ascii_uppercase)  
print(string.digits)
print(string.hexdigits) 
print(string.punctuation)

## Comparing string
# When comparing strings, ensure that both the strings are of the same case and contain the same characters in the same order, as the comparison is case-sensitive and character-sensitive.
str1 = "test"
str2 = "test1"
print(str == str1)

str3 = "test"
print(str1 == str3)

# Case- insensitive comparison - manner by converting both strings to either lower or upper case before comparison
str4 = "TEST"
print(str1.upper() == str4.upper())

# experiment with comparison operators
test = "c"
test1 = "h"

print(test > test1) # to understand how strings are compared lexicographically.
print(ord("c"))
print(ord("h"))


