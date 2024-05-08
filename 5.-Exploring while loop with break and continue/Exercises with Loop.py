## Coding Exercise: Is the Number Prime?
# In this exercise, you are tasked with creating a Python function named is_prime that determines whether a given integer is a prime number or not. A prime number is only divisible by 1 and itself.
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
           return False
        
    return True
              
print(is_prime(5)) 

## Coding exercise: Calculate the Sum of Squares Up to a Limit
# Your goal is to compute the sum of squares of numbers up to a specified limit.
def sum_of_squares_upto_limit(limit):
    i = 1
    sum = 0
    while i * i <= limit:
        sum += i * i
        i += 1
    return sum
 
print(sum_of_squares_upto_limit(30))

## Coding Exercise: Find the Number of Digits in a Number
# In this exercise, your task is to create a Python function named get_number_of_digits that determines the number of digits in a given integer.
def get_number_of_digits(number):
    if number < 0:
        return -1
        
    if number == 0:
        return 1
        
    number_of_digits = 0
    
    while number > 0:
        number = number // 10 
        number_of_digits += 1
        
    return number_of_digits
    
print(get_number_of_digits(123))
print(get_number_of_digits(9087))
print(get_number_of_digits(65))

## Coding Exercise: Finding the Next Fibonacci Number Exceeding a Threshold
# In this exercise, you are tasked with creating a Python function named next_fibonacci that identifies the first Fibonacci number that exceeds a given threshold, using a while loop.
def next_fibonacci(threshold):
    a, b = 0, 1
    sum = 0
    
    while True:
        sum = a +b
        
        if (sum > threshold):
            break 
    
        a = b
        b = sum 
        
    return sum
    
print(next_fibonacci(20))