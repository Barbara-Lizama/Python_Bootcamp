## Why We Need Data Structures
# Data structures are crucial when you need to store multiple values, like students' marks. Without a proper data structure, adding or removing students and calculating the sum and average becomes cumbersome.

mark1 = 45
mark2 = 54
mark3 = 80

print(mark1 + mark2 + mark3) 
print((mark1 + mark2 + mark3)/3)

mark4 = 43
print((mark1 + mark2 + mark3 + mark4)/3) 
print((mark1 + mark2 + mark3 + mark4)/4) 

## Python’s list data structure is versatile and powerful, with many built-in features and capabilities, making it an essential part of Python programming!
marks = [45, 54, 80]

print(sum(marks)) 
print(sum(marks)/len(marks)) 

marks.append(43)
print(sum(marks)/len(marks)) 
print(type(marks)) 

## Operations On List Data Structure
# Creating and Analyzing a List :
marks = [23, 56, 67]
print(sum(marks))  
print(max(marks))  
print(min(marks))  
print(len(marks)) 

# Adding and Removing Elements :
marks.append(76)
print(marks)  
 
marks.insert(2, 60)
print(marks)  

marks.remove(60)
print(marks)  

# Searching and Checking Existence :
print(55 in marks)  
print(56 in marks)  
print(marks.index(67))  
print(marks[3])
print(marks)  

### print(marks.index(69)) error, that does not exist in the list

# Iterating Through a List :
for i in marks:
    print(i)

## Puzzles with list of Strings
# Creating a list, finding lenght and access list elements. You can create a list by enclosing a comma-separated sequence of values within square brackets [].
animals = ['Cat', 'Dog', 'Elephant']
print(animals)
print(len(animals))
print(animals[2])
print(animals[0])

# Deleting an element from the list and extending a list.
del animals[2]
print(animals)

animals.extend(['Giraffe', 'Horse'])
print(animals)

animals += ['Lion', 'Monkey']
print(animals)

## Create a list containing different data types
mixed_list = [1, "Python", 3.14, ["another", "list"]]
print(len(mixed_list))
print(mixed_list[3])
del mixed_list[1]
mixed_list.extend(['Giraffe', 'Horse'])
print(mixed_list)

numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

## Sorting, Looping, and Reversing Lists
# you'll learn about the manipulation of lists, including their reversal, sorting, and how to loop through them using different techniques.

# Reversing a list
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.reverse()
print(numbers) 

for number in reversed(numbers):
    print(number)

# Sorting a list
numbers.sort()
print(numbers) 

for number in sorted(numbers):
    print(number)

for number in sorted(numbers, key=len):
    print(number)

for number in sorted(numbers, key=len, reverse=True):
    print(number)


