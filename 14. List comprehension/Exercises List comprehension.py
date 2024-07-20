## Coding Exercise: Slice and Double
# Given a list of integers and two indices, you'll extract a portion of the list using these indices and then double the numbers in that section. Make sure to handle cases where the indices are outside the list's boundaries.

def slice_and_double(numbers, a, b):
    if a < 0:
        a = 0
        
    if b > len(numbers):
        b = len(numbers)
        
    sliced_part = numbers[a:b]     
    
    doubled_slice = [x * 2 for x in sliced_part]
    
    numbers[a:b] = doubled_slice
    
    return numbers

print(slice_and_double([1, 2, 3, 4, 5], 1, 4))  
print(slice_and_double([10, 11, 12], 0, 2))
print(slice_and_double([7, 8, 9, 10], 1, 5))

## Coding Exercise: Extract Odd Numbers from a List
# In this exercise, you are tasked with creating a Python function named extract_odd_numbers that filters all the odd numbers from a given list of integers.

def extract_odd_numbers(values):
    if values ==  []:
       return []
    result = [value for value in values if value % 2 == 1]
    return result
    
print(extract_odd_numbers([3, 6, 9, 1, 4, 15, 6, 3]))
print(extract_odd_numbers([]))
print(extract_odd_numbers([2, 15, 68, 32, 7]))