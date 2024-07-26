### Introduction To Set
## Use sets when you need to work with unique elements, or perform operations like union, intersection, or difference.
# CREATING A SET
numbers_set = {1, 2, 3, 4}

# ADDING TO A SET
numbers_set.add(4)
print(numbers_set)  
numbers_set.add(0)
print(numbers_set)  

# REMOVING AN ELEMENT FROM THE SET
numbers_set.remove(0)
print(numbers_set)  

# SETS DO NOT SUPPORT ACCESS USING INDEX
#numbers_set[0]  # This will raise TypeError: 'set' object does not support indexing

# CHECK EXISTENCE OF AN ELEMENT IN A SET
print(1 in numbers_set)  
print(5 in numbers_set)  

# PERFORMING AGGREGATE OPERATIONS ON A SET
print(min(numbers_set))  
print(max(numbers_set))  
print(sum(numbers_set))  
print(len(numbers_set))  

# UNION INTERSECTION AND DIFFERENCE OF SETS
numbers_1_to_5_set = set(range(1,6))
print(numbers_1_to_5_set)  
numbers_4_to_10_set = set(range(4,11))
print(numbers_4_to_10_set)

print(numbers_1_to_5_set | numbers_4_to_10_set)  # union
print(numbers_1_to_5_set & numbers_4_to_10_set)  # intersection
print(numbers_1_to_5_set - numbers_4_to_10_set)  # difference or subtraction
print(numbers_4_to_10_set - numbers_1_to_5_set)  # difference or subtraction

### Unpacking Lists and Sets
## You can use the * operator to unpack elements from a list and pass them as arguments to a function.

# UNPACKING ELEMENTS FROM A LIST
def print_values(num1, num2, num3):
    print(num1)
    print(num2)
    print(num3)
 
numbers = [10, 20, 30]
print_values(*numbers)

# UNPACKING ELEMENTS FROM A SET
scores = {85, 90, 75}
print_values(*scores)

# Examples 

s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2) # Same as s1 | s2
print(result)
 
# Use set.union()
list_of_sets_1 = [set([1, 2]), set([3, 4]), set([5, 6])]
list_of_sets_2 = [set([5, 6]), set([7, 8])]
union_result = set.union(*list_of_sets_1, *list_of_sets_2) #similar functions exist for union and difference
print(union_result)
 
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.difference(s2) # Same as s1 - s2
print(result)
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {x**2 for x in numbers if x % 2 == 0}
print(result)
 
num = 5
result = {x for x in range(num, 101, num)}
print(result)
 
my_list = [1, 2, 3, 2, 1, 4, 5, 3]
result = set(my_list)
print(result)
 
string_1 = "hello"
string_2 = "world"
result = set(string_1) | set(string_2)
print(result)
 
list_of_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
result = set.intersection(*list_of_sets)
print(result)

head = [{1, 2, 3, 5}, {3, 4, 5}, {5, 6, 7}]
result = set.intersection(*head)
print(result)