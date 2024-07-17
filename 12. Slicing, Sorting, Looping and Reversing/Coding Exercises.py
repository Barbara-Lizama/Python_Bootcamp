## Coding Exercise: Slice Alternate Elements
# In this exercise, you are tasked with crafting a Python function, slice_alternate_elements, designed to fetch all the even-indexed elements originating from a list of integers.

def slice_alternate_elements(numbers):
    
    return numbers[::2]

print(slice_alternate_elements([5, 12, 19, 26, 33, 40]))  # Expected Output: [10, 30, 50]
print(slice_alternate_elements([]))

## Coding Exercise: Reverse Each Chunk
# In this exercise, your task is to create a Python function named reverse_chunks that reverses every three elements in a given list of integers.

def reverse_chunks(numbers):
    for i in range(0, len(numbers), 3):
        numbers[i:i+3] = numbers[i:i+3][::-1]
    
    return numbers 
    
print(reverse_chunks([6, 12, 18, 7, 14, 21, 9, 18, 27]))  

## Coding Exercise: Reorder and Eliminate Middle
# In this exercise, you are tasked with creating a function that sorts a list of strings based on their length in descending order and then removes the middle element(s). If the list has an odd number of elements, you'll remove the exact middle element. If the list has an even number of elements, you'll remove the two middle elements.

def reorder_and_eliminate_middle(words):
    if len(words) <= 2:
        return []
        
    sorted_words = sorted(words, key=len, reverse=True)
    
    middle = len(sorted_words) // 2
    
    if len(sorted_words) % 2 == 0:
        del sorted_words[middle - 1 : middle + 1]
    else:
        del sorted_words[middle]
    
    return sorted_words
    
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"])) 
print(reorder_and_eliminate_middle(["dali", "rabbit", "george", "dog"]))