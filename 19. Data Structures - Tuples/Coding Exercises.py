## Coding Exercise: Tuple Swapping
# In this exercise, your task is to create a Python function named swap_elements that swaps the first and last elements of a given tuple.

def swap_elements(input_tuple):
    return input_tuple[-1], *input_tuple[1:-1], input_tuple[0]

print(swap_elements((7, 14, 21, 28)))     
print(swap_elements(('apple', 'banana', 'cherry', 'rabbit'))) 
print(swap_elements((5, 10)))

## Coding Exercise: Count Occurrences in Tuple
# In this exercise, your task is to design a Python function named count_occurrences that quantifies how many times a specific element can be found in a given tuple.

def count_occurrences(input_tuple, target):
    return input_tuple.count(target)
    
print(count_occurrences(('rabbit', 'dog', 'dali', 'cat', 'raccon'), 'dali'))    
print(count_occurrences((1, 2, 2, 3, 2), 2))   
print(count_occurrences((6, 12, 18, 24, 30), 10))

## Coding Exercise: Student Grade Summary
# In this exercise, your task is to create a Python function named student_summary that processes a tuple containing student details and returns a formatted summary string describing the student.

def student_summary(student):
    name, age, grade = student
    return f"Student Name: {name}, Age: {age}, Grade: {grade}" 
    
print(student_summary(('Alice', 20, 89.5)))  
print(student_summary(('Charlie', 19, 92.0)))

## Coding Exercise: Distance Between Points
# Your task is to write a Python function named calculate_distance that computes the Euclidean distance between two given points, which are represented as tuples.

import math 

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
 
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return distance
    
print(calculate_distance((1.0, 2.0), (4.0, 6.0)))  
print(calculate_distance((0.0, 0.0), (0.0, 5.0)))  