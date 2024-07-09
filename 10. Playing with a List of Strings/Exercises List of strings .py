## Coding Exercise: Rotate List of Strings 'n' Times
# In this exercise, your task is to create a Python function named rotate_strings that takes a list of strings and a positive integer n as inputs. The function should rotate the list n times to the right and return the rotated list.

def rotate_strings(strings, n):
    if not strings or n == 0:
        return strings
        
    for _ in range(n):
        last_element = strings[-1]
        for i in range(len(strings)- 1, 0, -1):
            strings[i]= strings[i - 1]
        strings[0] = last_element
    return strings
    
print(rotate_strings(['a', 'b', 'c'], 2))     
print(rotate_strings(['apple', 'banana', 'cherry', 'date'], 1))   
print(rotate_strings(['hello', 'world'], 3))    

## Coding Exercise: Encode List of Strings
# In this exercise, your task is to create a Python function named encode_strings that takes a list of strings as input. The function should replace each string in the list with a new string where each character is replaced by the next character in the ASCII table. Return the encoded list.

def encode_strings(strings):
    encoded_list = []

    for string in strings:
        encoded_string = ''

        for char in string:
            if char == 'z':
                encoded_char = 'a'
            elif char == 'Z':
                encoded_char = 'A'
            else:
                encoded_char = chr(ord(char) + 1)

            encoded_string = encoded_string + encoded_char

        encoded_list.append(encoded_string)

    return encoded_list
    
print(encode_strings(['abc', 'def']))  
print(encode_strings(['rabbit', 'raccoon']))  # Output: ['ifmmp', 'XPSME']
print(encode_strings(['dali']))  # Output: ['app']
print(encode_strings(['']))  # Output: ['']

## Coding Exercise: Alternate Merge of Two Lists
# In this exercise, you're tasked with merging two lists by alternating elements from each list. If one list is longer than the other, the excess elements should be added to the end of the merged list.

def alternate_merge(list1, list2):
    merged_list = []

    max_length = max(len(list1), len (list2))
    
    for i in range(max_length):
        
        if i < len(list1):
            merged_list.append(list1[i])
        if i < len(list2):
            merged_list.append(list2[i]) 
            
    return merged_list
       
print(alternate_merge(['a', 'b'], ['c', 'd', 'e'])) 
print(alternate_merge(['dali', 'little', 'good'], ['rabbit', 'netherland']))

## Coding Exercise: Anagram Checker using List
# In this exercise, your task is to create a Python function named is_anagram that checks if two given strings are anagrams of each other.
# CONSTRAINT: You should NOT sort the strings. Create two lists of 26 zeros each, list1 and list2 storing the occurrences of each character. Use this list to compare and find if the strings are anagrams.

def is_anagram(string1, string2):
    
    if len(string1) != len(string2):
        return False
        
    list1 = [0] * 26
    list2 = [0] * 26
        
    for char in string1:
            list1[ord(char) - ord ('a')] += 1
            
    for char in string2:
            list2[ord(char) - ord ('a')] += 1    
        
    return list1 == list2

print(is_anagram("hello", "hey"))
print(is_anagram("listen", "silent"))
print(is_anagram("dog", "god"))