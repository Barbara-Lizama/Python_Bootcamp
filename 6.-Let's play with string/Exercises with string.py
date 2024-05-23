## Coding Exercise: Is it a Vowel?
# In this exercise, your task is to create a Python function named is_vowel that determines whether a given character is a vowel or not.

def is_vowel(char):
    vowel_string = 'aeiouAEIOU'
    
    if char in vowel_string:
       return True
    else :
        return False
    
print(is_vowel('a'))
print(is_vowel('b'))
print(is_vowel('E'))

## Coding Exercise: Count Uppercase Letters
# In this exercise, your task is to create a Python function named count_uppercase_letters that counts the number of uppercase letters in a given string.
import string

def count_uppercase_letters(text):
    count = 0 
    
    for char in text:
        if char in string.ascii_uppercase:
            count += 1
    return count
     
print(count_uppercase_letters('Hello WORLD'))
print(count_uppercase_letters('WELcome haWAIi'))

## Coding Exercise: Check Consecutive Identical Characters
# In this exercise, your task is to create a Python function named has_consecutive_identical_characters that checks if a given string has at least two consecutive identical characters.

def has_consecutive_identical_characters(text):

    for i in range (0, len(text) - 2):
        if (text [i] == text [i + 1]):
            return True

    return False
        
print(has_consecutive_identical_characters('Hello World'))
print(has_consecutive_identical_characters('WELcome Kauai')) 

## Coding Exercise: Find the Right-most Digit
# In this exercise, your task is to create a Python function named find_right_most_digit that returns the right-most digit found in a given string.

def find_right_most_digit(text):

    for char in reversed(text):
        if char.isdigit():
            return int(char)

    return -1

print(find_right_most_digit('The value is 85'))  
print(find_right_most_digit('Very good'))  

## Coding Exercise: Find the Longest Word
# Create a Python function named find_longest_word that identifies and returns the left-most longest word in a provided text.

def find_longest_word(text):

    x = text.split()
    lenght = 0
    finalText = ''
    
    for i in x:
        if len(i) > lenght:
            lenght = len(i)
            finalText = i

    return finalText
    
print(find_longest_word('The quick brown fox jumps over the lazy dog'))  
print(find_longest_word(''))  
print(find_longest_word('Chicho is very beatiful'))  

## Coding Exercise: Anagram Checker
# In this exercise, your task is to create a Python function named is_anagram that checks whether two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
# You can assume that the input strings only contain lowercase alphabets, so there is no need to worry about case sensitivity or non-alphanumeric characters.

def is_anagram(string1, string2):
    
    if sorted(string1) == sorted(string2):
       return True
    else :
        return False
    
print(is_anagram('listen', 'silent'))
print(is_anagram('married', 'admirer'))  
print(is_anagram('rabbit','rodient'))

## Coding Exercise: Is Hex String?
# In this exercise, your task is to create a Python function named is_hex_string that checks whether a given string consists solely of valid hexadecimal characters. An empty string should not be considered as a valid hex string.

def is_hex_string(string):
    if string == '':
        return False
        
    hex_digits ='0123456789abcdefABCDEF'
    
    for char in string:
        if char not in hex_digits:
            return False
    
    return True
            
print(is_hex_string('1a2f4C'))  
print(is_hex_string('1g2f4C'))  
print(is_hex_string('dali'))         
    
## Coding Exercise: Word Reverser using For Loop
# In this exercise, your task is to create a Python function named reverse_word that takes a string as input and returns the reversed version of the string.

def reverse_word(word):
    reversed_word = ''
    
    for char in word:
        reversed_word = char + reversed_word 
    return reversed_word
        
print(reverse_word("Python"))
print(reverse_word("Rabbit"))

## Examples with String

data = "Life is pretty"
print(type(data))
 
char = 'e'
count = 0
for c in "Paralelepipedo":
    if c == char:
        count += 1
print(count)
 
str1 = "berries"
str2 = "pineapple"
print(str1 < str2)
 
text = "Rabbit "
repeated_text = text * 3
print(repeated_text)
 
str1 = "Happy"
str2 = " Birthday"
result = str1 + str2
print(result)
 
str1 = "Happy"
str2 = "Birthday"
print(len(str1) == len(str2))

## Repeating Strings 
# Multiplying a Number
print(3 * 5)
print(2 * 20)

# Repeating a String
print('3' * 8) 
print('6' * 3) 

# Repeating Different Characters
print('dali' * 5)
print('T' * 4)