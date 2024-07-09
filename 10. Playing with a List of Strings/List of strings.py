## Playing with ASCII Values
# Getting started with ASCII: Each character on a keyboard (letters, numbers, punctuation marks, etc.) corresponds to a unique number in the ASCII table.

# Using ord(char) function
# The ord() function in Python takes a single character as an argument and returns its ASCII value.
ascii_value_V = ord('V')
ascii_value_a = ord('a')
ascii_value_1 = ord('1')
print(ascii_value_V)
print(ascii_value_a)
print(ascii_value_1)

# Getting the next ASCII value
# To get the next ASCII value of a character, you can simply add 1 to its ASCII value.
char = '5'
next_ascii_value = ord(char) + 1
print(f"The next ASCII value after {char} is: {next_ascii_value}")

# Converting ASCII value to character
# It provides the chr() function for this purpose.
ascii_val = 37
character = chr(ascii_val)
print(character)

## Working with Lists of Custom Types
# we will explore how to work with a list of a custom type. We'll be using a Country class as an example.
# Creating Country Class

class Country:
 
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
 
    def __repr__(self):
        return repr((self.name,self.population,self.area))

countries = [Country('India',1200,100),
             Country('China', 1400, 200),
             Country('USA', 120, 300)]
print(countries)

countries.append(Country('Russia',80,900))
print(countries)

from operator import attrgetter 
countries.sort(key=attrgetter('population'), reverse=True)
print(countries)

print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('area')))
print(max(countries, key=attrgetter('area')))

## Exploring Variable arguments
# Using *args

def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value
result = find_max(3, 8, 2, 10, 5)
print(result)

# Combining strings

def combine_strings(*args):
    return ' '.join(args)
result = combine_strings('Hello', 'world', 'from', 'Python')
print(result)  # Outputs: Hello world from Python


