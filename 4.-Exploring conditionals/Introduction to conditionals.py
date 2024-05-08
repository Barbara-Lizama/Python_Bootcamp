## Basic if statement
i = 5
if i>3:
    print(f"{i} is greater than 3")

## Comparing values with if statements
a = 5
b = 7
 
if(a>b):
    print("a is greater than b") ## will not be executed because is false

b = 7 
a = 9
 
if(a>b):
    print("a is greater than b") ## will be executed because is true

## Coding exercise: Check for a valid triangle
## In this exercise, your task is to create a Python function named is_valid_triangle that returns if the three given angles can form a valid triangle. 
## An angle cannot be less than or equal to 0.
def is_valid_triangle(angle1, angle2, angle3):
    if angle1 <= 0:
        return False
        
    if angle2 <= 0:
        return False 
        
    if angle3 <= 0:
        return False  
        
    result = (angle1 + angle2 + angle3) == 180
    
    return result   
       
print(is_valid_triangle(30, 60, 90))

## Coding exercise: Calculate the sum of divisors
## In this exercise, your task is to create a Python function named calculate_sum_of_divisors that calculates the sum of all divisors of a given integer number.
def calculate_sum_of_divisors(number):
    sum = 0
    if number <= 0:
        return sum 
        
    for i in range(1, number + 1):
        if number % i == 0:
            sum += i
        
    return sum   
print(calculate_sum_of_divisors(6))
print(calculate_sum_of_divisors(15))

## Coding exercise: Check if a number is a perfect number
## In this exercise, your task is to create a Python function named is_perfect_number that checks whether a given integer is a perfect number or not.
## A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself.
def is_perfect_number(number):
    divisor_sum = 0
    
    if number <= 0:
        return divisor_sum
        
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
            
    if divisor_sum == number:
        return True
    else :
        return False

print(is_perfect_number(6)) 
print(is_perfect_number(28))
print(is_perfect_number(5))

## Coding exercise: Find last digit of a number
## In this exercise, your task is to create a Python function named get_last_digit that finds the last digit of a given integer.
def get_last_digit(number):
    last_digit = number % 10
    
    return last_digit
    
print(get_last_digit(123))
print(get_last_digit(9087))
print(get_last_digit(6))