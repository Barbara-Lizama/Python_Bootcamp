## Coding Exercise: Is There a Greater Element?
# In this exercise, your task is to create a Python function named has_greater_element that checks whether there is any number greater than a given value in a list of numbers.

def has_greater_element(numbers, value):
    if numbers == [] :
        return False
        
    for i in numbers:
        if i > value:
            return True
    return False
    
print(has_greater_element([10, 20, 30], 15))      
print(has_greater_element([5, 7, 8], 10))       
print(has_greater_element([], 5))      

## Coding Exercise: Are Sum of Two Lists Equal?
# In this exercise, your goal is to determine if the sum of the elements in two given lists is equal, without resorting to built-in functions (like sum).

def are_sums_equal(list1, list2):
    if list1 == []:
        return False
    if list2 == []:
        return False
        
    sum1 = 0
    sum2 = 0
    
    for i in list1:
        sum1 += i 
        
    for j in list2:
        sum2 += j
        
        if sum1 == sum2:
           return True
       
    return False
        
print(are_sums_equal([10, 20, 30], [15, 25, 20]))  
print(are_sums_equal([5, 10, 15], [5, 10, 14]))  
print(are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1]))  
print(are_sums_equal([], [4, 3, -7]))  
print(are_sums_equal([1, 2], []))  

## Coding Exercise: Check if List is Sorted
# In this exercise, your mission is to determine whether a provided list of integers is sorted in ascending order.

def is_list_sorted(list):
    if list == []:
        return True
        
    for i in range(len(list) - 1):
        if list[i] > list [i + 1]:
           return False
        
    return True   
               
print(is_list_sorted([7, 14, 21]))   
print(is_list_sorted([10, 21, 20]))   
print(is_list_sorted([3, 20, 10]))   
print(is_list_sorted([]))  

## Coding Exercise: Reverse a List Using Two-Pointer Approach
# In this exercise, your objective is to construct a Python function titled reverse_list that inverts a given list of integers. The unique aspect of this exercise is the use of the two-pointer technique without resorting to any built-in Python functionalities.

def reverse_list(list):
    start = 0
    end = len(list) - 1
    
    while start < end:
        list[start], list[end] = list[end], list[start]
        
        start += 1
        end -= 1

    return list    

print(reverse_list([10, 20, 80,30]))      
print(reverse_list([5, 13, 25, 45]))   
print(reverse_list([1]))    

## Coding Exercise: Find All Factors of a Number
# In this exercise, your task is to create a Python function named find_factors that determines all the factors of a given integer.

def find_factors(number):
    factors = []
    
    for i in range(1, number + 1):
        if number % i == 0:
           factors.append(i)
            
    return factors
    
print(find_factors(12))  
print(find_factors(15))  
print(find_factors(28))   

## Coding Exercise: List of Multiples
# In this exercise, you are tasked with creating a Python function named find_multiples. This function should determine all the multiples of a given number that are less than a provided limit.

def find_multiples(number, limit):
    multiples = []
    
    current = number
    
    while current < limit:
          multiples.append(current)
          current += number
          
    return multiples  

print(find_multiples(3, 10))
print(find_multiples(5, 22))
print(find_multiples(4, 34))
print(find_multiples(7, 16))

