## Coding Exercise: Counting Character Occurrences
# In this exercise, your challenge is to craft a Python function called count_characters that processes an input string and returns a dictionary. This dictionary should detail the frequency of each character present in the string.
 
def count_characters(str):
    char_occurances = {}
    
    for char in str:
        char_occurances[char] = char_occurances.get(char, 0) + 1
    return char_occurances
       
print(count_characters("apple"))
print(count_characters("rabbit"))
print(count_characters("This is an awesome occasion."))

## Coding Exercise: Counting Word Occurrences
# In this exercise, you'll create a function named count_words(str)  that counts the number of occurrences of each word in a given string.

def count_words(str):
    word_occurrences = {}
    
    words = str.split()
    
    for word in words:
        word_occurrences [word] = word_occurrences.get(word, 0 ) + 1
        
    return word_occurrences
    
print(count_words("This is an example.")) 
print(count_words("Hello world! Hello everyone."))

## Coding Exercise: Map with Squares of First n Numbers
# In this exercise, your task is to create a Python function named squares_map that returns a dictionary containing the squares of the first n natural numbers. The keys should be the numbers themselves, and the values should be the corresponding squares.

def squares_map(n):
    squares = {x: x**2 for x in range(1, n + 1)}
    return squares
    
print(squares_map(10))
print(squares_map(7))

## Coding Exercise: Find Common Subjects
# In this exercise, you are tasked with creating a Python function, common_subjects, that identifies the subjects that are studied by all students across three different grades.

def common_subjects(grade1, grade2, grade3):
    if not grade1 or not grade2 or not grade3:
        return set()
        
    all_grades = [grade1, grade2, grade3]
    for grade in all_grades:
        for subjects in grade.values():
            if not subjects:
                return set()
                
    common_grade1 = set.intersection(*grade1.values())
    common_grade2 = set.intersection(*grade2.values())
    common_grade3 = set.intersection(*grade3.values())
    return common_grade1 & common_grade2 & common_grade3


grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": {}, "Hank": {"History"}}
 
print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()

