## Introduction To List Comprehension
# List comprehension is a concise way to create lists

# Creating lists in a traditional approach
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
 
numbers_length_four = []
 
for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)
 
print(numbers_length_four)

# Creating Lists using list comprehension
numbers_length_four = [number for number in numbers if len(number) == 4]
 
print(numbers_length_four)

# Examples with List Comprehension
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
result = [name for name in names if 'e' in name]
print(result)  
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num for num in numbers if num % 2 == 0]
print(result)  
 
sentence = "The quick brown fox jumps over the lazy dog"
result = [char for char in sentence if char.lower() in 'aeiou']
print(result)  
 
original_list = [1, 2, 3, 4, 5]
result = [num**2 for num in original_list]
print(result)  
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num**2 for num in numbers if num % 2 != 0]
print(result)  
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(result)  
 
sentence = "Hello World! How are you doing?"
result = [len(word) for word in sentence.split()]
print(result)