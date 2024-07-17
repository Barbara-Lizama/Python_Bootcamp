## Introduction to List slicing
# List slicing is a powerful feature in Python, allowing you to extract portions of a list with minimal code. It significantly enhances code readability and simplicity.
# Getting started with basics of slicing
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
 
print(len(numbers))  
print(numbers[3])    
print(numbers[1:5])  

# Can omit start or end index
print(numbers[:7])  
print(numbers[2:])

# Exploring the step parameter
print(numbers[2:9:2])  
print(numbers[3:10:5])  
print(numbers[::3])

# Let's reverse a list
print(numbers[::-2])  
print(numbers[::-5])

# Can delete elements using slicing
del numbers[5:]
print(numbers)  

# Can replace elements using slicing
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[3:7] = [3, 4, 5, 6]
print(numbers)

