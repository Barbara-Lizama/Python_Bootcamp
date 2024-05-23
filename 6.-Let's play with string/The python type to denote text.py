## Examples denote text
print("Hello World")
print('Hello World')

## # Do not mix single and double quotes - this will throw an error: print('Hello World")  # SyntaxError

## Finding the type of a string
comment = "Dali tierno"
print(type(comment))

## String utility methods
# Converting to uppercase and lowercase
comment = "welcome hawaii"
print(comment.upper())  
print(comment.lower())  
print("welcome hawaii".capitalize())  

# Checking lower case, title case and upper case
print('hello'.islower())  
print('Hawaii'.islower())  
print('Dali'.istitle())  
print('rabbit'.istitle())  
print('lily'.isupper())  
print('VITAMIN'.isupper())  

# Checking if a string is a numeric value
print('123'.isdigit())  
print('A23'.isdigit())  
print('2 3'.isdigit())  
print('23'.isdigit())   

# Checking if a string only contains alphabets or alphabets and numerals
print('51'.isalpha())   
print('2t'.isalpha())   
print('tea'.isalpha())  
print('dali5'.isalnum())  
print('ABC 123'.isalnum())  

# Checking if a string ends or starts with a specific substring
print('VITAMIN'.endswith('MIN'))   
print('rabbit'.endswith('old'))     
print('Hello World'.startswith('Wo'))    
print('Dali'.startswith('Da'))    

# Finding a substring within a string
print('Hello World'.find('Hello'))  
print('Hello World'.find('ello'))   
print('Hello World'.find('Ello'))    
print('Hello World'.find('Wor'))    

# Using in keyword to check in a string
print('Hllo' in 'Hello World')
print('Hawai' in 'Hawaii')
print('Butter' in 'Butterfly')

## Python has no separate character type
# There is no distinct data type for single characters. Both strings and single characters are represented by the str class.
comment = "welcome hawaii"
print(comment[8])
print(type(comment[0]))
## print(comment[20]) ## Error details: string index out of range

for ch in comment:
    print(ch)







